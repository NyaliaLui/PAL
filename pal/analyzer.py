from time import sleep
from os import listdir
from os.path import join
from data_collector import DataCollector

#Analyzer
# @purpose - a singleton which starts the analysis engine. This involves monitoring the replay folder and communicating
# with PAL servers.
class Analyzer:

    def __init__(self, folder, n, json_enabled):
        self.__folder = folder
        self.__n = n
        self.__json_enabled = json_enabled
        self.__collector = DataCollector()

        #get replays currently in the folder
        self.__current = [join(folder, f) for f in listdir(self.__folder)]

        #collect data on those replays
        self.__collector.collect(self.__current)

        #send data to PAL server(s)
        self.__collector.send()


    #run
    # @params - no parameters
    # @return - no return values
    # @purpose - executes the ladder analyzer
    def run(self):
        while 1:
            sleep(self.n_)

            #were replays added to the directory?
            after = [f for f in listdir(self.__folder)]
            added = [f for f in after if not f in self.__current]
            if added: print "Ready to collect on ", ", ".join (added)

            #collect data on new replays
            self.__collector.collect(added)

            #send data to PAL server(s)
            self.__collector.send()

            #update local record
            self.__current = after