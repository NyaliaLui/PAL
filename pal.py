#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import argparse
from pal import Analyzer

parser = argparse.ArgumentParser(description='A python script that collects data on your sc2 ladder games in the current season. See github.com/PAL for more info.')
parser.add_argument('folder', type=str, help='path to folder of replays to collect information from')
parser.add_argument('--sc2name', type=str, required=True, help='name of the sc2 player that is using this service')
parser.add_argument('-n', type=int, default=60, help='Check the folder every N seconds')

args = parser.parse_args()

try:
    #run the ladder analyzer
    analyzer = Analyzer(args.folder, args.n, args.sc2name)
    analyzer.run()
except Exception as ex:
    print('Something went wrong: {0}'.format(ex))
