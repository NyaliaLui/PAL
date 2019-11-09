#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import os, time
import sys
import argparse

#Analyzer
# @purpose - a singleton which starts the analysis engine. This involves monitoring the replay folder and communicating
# with PAL servers.
class Analyzer:

    def __init__(self, folder, n, json_enabled):
        self.folder_ = folder
        self.n_ = n
        self.json_enabled_ = json_enabled

    def run(self):
        before = dict ([(f, None) for f in os.listdir (self.folder_)])
        while 1:
            time.sleep (self.n_)
            after = dict ([(f, None) for f in os.listdir (self.folder_)])
            added = [f for f in after if not f in before]
            removed = [f for f in before if not f in after]
            if added: print "Added: ", ", ".join (added)
            if removed: print "Removed: ", ", ".join (removed)
            before = after

parser = argparse.ArgumentParser(description='A python script that collects data on your sc2 ladder games in the current season. See github.com/PAL for more info.')
parser.add_argument('folder', type=str, help='path to folder of replays to collect information from')
parser.add_argument('-n', type=int, default=60, help='Check the folder every N seconds')
parser.add_argument('--json', action='store_true', help='Create json files of the data collected. off by default')

args = parser.parse_args()

#annonce which sort option was chosen
if args.json:
    print("Create json files enabled")

try:
    #run the ladder analyzer
    analyzer = Analyzer(args.folder, args.n, args.json)
    analyzer.run()
except Exception as ex:
    print('Something went wrong: {0}'.format(ex))
