from replay import Replay

#DataCollector
# @purpose - responsible for collecting necessary data on ladder matches and sending them
#to PAL server(s)
class DataCollector:

    def __init__(self):
        self.__replays = []

    #collect
    # @params - list of replay file names with paths
    # @return - no return values
    # @purpose - extracts all relevant data on a ladder match via the SC2Replay file.
    #This uses the s2protocol. See github.com/PAL/collected_data.md for what data gets collected.
    def collect(self, replay_files):

        if len(replay_files) < 1:
            raise Exception('DataCollector.collect(): no replay files supplied')
        
        # for file_path in replay_files:
        #     replay = Replay(file_path)
        #     self.__replays.append(replay)
        replay = Replay(replay_files[0])
        self.__replays.append(replay)

    #send
    # @params - no parameters
    # @return - no return values
    # @purpose - sends a list of updated data to PAL server(s)
    def send(self):

        #send to match history db

        #send to player name db

        #send to map db

        #send to date db

        for replay in self.__replays:
            print(replay.json())