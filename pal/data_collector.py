from replay import Replay

#DataCollector
# @purpose - responsible for collecting necessary data on ladder matches and sending them
#to PAL server(s)
class DataCollector:

    def __init__(self):
        pass

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
            replay = Replay(file_path)
            updated.append(replay)

        return updated

    #send
    # @params - list of replay data to send to PAL server(s)
    # @return - no return values
    # @purpose - sends a list of replay data to PAL server(s)
    def send(self, replay_data):

        #We intend to create mongodb server and we will collect
        #the necessary information on that server dynamically when the route is loaded

        #currently just printing to screen in json format because I don't
        #have a mongo server setup
        for replay in replay_data:
            print(replay.json())