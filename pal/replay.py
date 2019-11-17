from s2protocol import versions
import mpyq
import sys
from os.path import isfile
from copy import deepcopy
from datetime import datetime

#is_replay
# @params - relative path to the replay file
# @return - returns true if file is a replay
# @purpose - determine if a file is a SC2 replay
def is_replay(replay_path):
    ret = (isfile(replay_path) and ('.SC2Replay' in replay_path[-10:]))
    return ret

#create_player
# @params - the name, SC2 race, clan (optional), and team (optional) for a player
# @return - returns the SC2 player in JSON format
# @purpose - construct a SC2 player as JSON object
# {
#    'name': player's name,
#    'race': one of three SC2 races,
#    'mmr': player's mmr
#    'result': win/loss
#    'clan_tag': clan name if applicable
#    'team_id': which lobby team the player is on
# }
def create_player(name, race, win, clan='', team=0):
    return { 'name': name, 'race': race, 'win': win, 'clan_tag': clan, 'team_id': team }

#Replay
# @purpose - a wrapper around S2 protocol replay files
class Replay:

    #player - The player who is using this software
    #opponent - The opponent in the replay
    #archive - the mpyq archive of the replay
    #baseBuild - the base build of the replay according to s2protocol
    #header - the replay header information
    #protocol - the protocol for this replay
    #details - the list of details for this replay in JSON format
    #local_path - the relative path to the replay
    #UTC_timestamp - the replay timestamp in UTC time
    #map - the sc2 map this was played on

    def __init__(self, sc2name, replay_path = ''):
        self.local_path = replay_path
        self.player = None
        self.opponent = None
        self.UTC_timestamp = 0
        self.is_comp = False
        self.map = ''
        self.map_code = ''

        __archive = None
        __baseBuild = None
        __header = None
        __protocol = None
        __details = None

        if replay_path is not '':
            #generate MPQ archive
            __archive = mpyq.MPQArchive(replay_path)
            
            #get the replays protocol version
            contents = __archive.header['user_data_header']['content']
            __header = versions.latest().decode_replay_header(contents)

            # The header's baseBuild determines which protocol to use
            #part of this code was modified from 
            #s2_cli.py @ https://github.com/Blizzard/s2protocol/tree/master/s2protocol
            __baseBuild = __header['m_version']['m_baseBuild']
            try:
                __protocol = versions.build(__baseBuild)
            except Exception, e:
                raise Exception('Unsupported base build: {0} ({1})'.format(__baseBuild, str(e)))

            #replay details
            try:
                contents = __archive.read_file('replay.details')
                __details = __protocol.decode_replay_details(contents)
                self.map = __details['m_title']
                self.map_code = self.map.replace(' ','-').lower()
                self.UTC_timestamp = __details['m_timeUTC']
            except Exception, e:
                raise Exception('Issue in extracting replay details')

            #replay initdata
            try:
                contents = __archive.read_file('replay.initData')
                initdata = __protocol.decode_replay_initdata(contents)
                game_desc = initdata['m_syncLobbyState']['m_gameDescription']
                game_options = game_desc['m_gameOptions']
                self.is_comp = game_options['m_competitive'] and not game_options['m_cooperative'] and not game_desc['m_isCoopMode'] and game_desc['m_maxUsers'] == 2
            except Exception, e:
                raise Exception('Issue in extracting replay init data')

            try:
                #pre process for matchup and names
                num_players = len(__details['m_playerList'])
                for i in range(num_players):
                    name = __details['m_playerList'][i]['m_name']
                    race = __details['m_playerList'][i]['m_race']
                    clan = ''
                    team = __details['m_playerList'][i]['m_teamId']
                    result = __details['m_playerList'][i]['m_result']

                    if name.find('&lt;') > -1:
                        info = self.__beautify_name(name)
                        clan = info[0]
                        name = info[1]

                    if sc2name == name:
                        self.player = create_player(name, race, result == 1, clan, team)
                    else:
                        self.opponent = create_player(name, race, result == 1, clan, team)
            except Exception, e:
                raise Exception('Issue in replay processing')

    #beautify_name
    # @params - the human readable name
    # @return - the clan tag and player name in an easier to read format
    # @purpose - SC2 Replays put HTML tags with player names, this function removes those characters.
    def __beautify_name(self, name):
        infos = name.split('<sp/>')
        infos[0] = infos[0].replace('&lt;', '')
        infos[0] = infos[0].replace('&gt;', '')
        infos[0] = '[' + infos[0] + ']'

        return infos

    #json
    # @params - no parameters
    # @return - returns the relevant replay information in json format
    # @purpose - convert the relevant replay information to json format
    def json(self):
        #for MS Windows, time ticks start Jan 1, 1970
        tick_start = 116444736000000000
        nano_seconds = 10000000
        dt_str = str(datetime.fromtimestamp((self.UTC_timestamp - tick_start) // nano_seconds))
        dt_str = dt_str.split()[0]

        return {'player': self.player, 'opponent': self.opponent,
         'timestamp': self.UTC_timestamp, 'date': dt_str, 'competitive': self.is_comp,
         'map': self.map, 'mcode': self.map_code}

#copy_replay
# @params - the SC2 replay
# @return - a copy of the SC2 replay
# @purpose - create a duplicate copy of the given SC2 replay
def copy_replay(name, replay):
    duplicate = Replay(sc2name=name)

    duplicate.series_flag = replay.series_flag
    duplicate.players = replay.players[:]
    duplicate.archive = deepcopy(replay.archive)
    duplicate.baseBuild = replay.baseBuild
    duplicate.header = deepcopy(replay.header)
    duplicate.protocol = replay.protocol
    duplicate.details = deepcopy(replay.details)
    duplicate.local_path = replay.local_path[:]
    duplicate.UTC_timestamp = replay.UTC_timestamp

    return duplicate
