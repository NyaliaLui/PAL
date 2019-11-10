from replay import Replay
from pymongo import MongoClient

#DataCollector
# @purpose - responsible for collecting necessary data on ladder matches and sending them
#to PAL server(s)
class DataCollector:

    def __init__(self, sc2name):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client.PAL
        self.__sc2name = sc2name

    #collect
    # @params - list of replay file names with absolute paths
    # @return - list of SC2 replays with necessary data
    # @purpose - extracts all relevant data on a ladder match via the SC2Replay file.
    #This uses the s2protocol. See github.com/PAL/collected_data.md for what data gets collected.
    def collect(self, replay_files):

        if len(replay_files) < 1:
            raise Exception('DataCollector.collect(): no replay files supplied')

        updated = []
        
        for file_path in replay_files:
            replay = Replay(self.__sc2name, file_path)
            updated.append(replay)

        return updated

    #send
    # @params - list of replay data to send to PAL server(s)
    # @return - no return values
    # @purpose - sends a list of replay data to PAL server(s)
    def send(self, replay_data):

        for replay in replay_data:
            rep_json = replay.json()
            self.__db.mhistory.insert_one(rep_json)