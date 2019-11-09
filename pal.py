#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import argparse
from pal import Analyzer

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
