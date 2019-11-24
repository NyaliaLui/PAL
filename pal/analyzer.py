from time import sleep
from os import listdir
from os.path import join
from .data_collector import DataCollector

#Analyzer
# @purpose - a singleton which starts the analysis engine. This involves monitoring the replay folder and communicating
# with PAL servers.
class Analyzer:

    def __init__(self, folder, n, sc2name):
        self.__folder = folder
        self.__n = n
        self.__collector = DataCollector(sc2name)

        #get replays currently in the folder
        self.__current = [join(folder, f) for f in listdir(self.__folder)]

        #collect data on those replays
        replays = self.__collector.collect(self.__current)

        #send data to PAL server(s)
        self.__collector.send(replays)


    #run
    # @params - no parameters
    # @return - no return values
    # @purpose - executes the ladder analyzer
    def run(self):
        while 1:
            sleep(self.__n)

            #were replays added to the directory?
            after = [join(self.__folder, f) for f in listdir(self.__folder)]
            added = [join(self.__folder, f) for f in after if not f in self.__current]

            if added:
                print("Ready to collect on ", ", ".join (added))

                #collect data on new replays
                replays = self.__collector.collect(added)

                #send data to PAL server(s)
                self.__collector.send(replays)

                #update local record
                self.__current = after

    #run_one_time
    # @params - no parameters
    # @return - no return values
    # @purpose - executes the ladder analyzer one time
    def run_one_time(self):
        #were replays added to the directory?
        after = [join(self.__folder, f) for f in listdir(self.__folder)]
        added = [join(self.__folder, f) for f in after if not f in self.__current]

        if added:
            print("Ready to collect on ", ", ".join (added))

            #collect data on new replays
            replays = self.__collector.collect(added)

            #send data to PAL server(s)
            self.__collector.send(replays)

            #update local record
            self.__current = after