#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import argparse
import json
from pal import Replay

parser = argparse.ArgumentParser(description='A python script that extract W/L data from a single replay.')
parser.add_argument('replay', type=str, help='path to the single SC2 Replay')
parser.add_argument('--sc2name', type=str, required=True, help='name of the sc2 player that is using this service')


args = parser.parse_args()

try:
    #run the ladder analyzer
    replay = Replay(args.sc2name, args.replay)
    print(json.dumps(replay.json()))
except Exception as ex:
    print('Something went wrong: {0}'.format(str(ex)))
