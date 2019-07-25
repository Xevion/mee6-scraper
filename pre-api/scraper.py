from _parser import *

Board = Leaderboard(120)
import json, os, sys
with open(os.path.join(sys.path[0], 'data.json'), 'w+') as data:
    json.dump(Board.get(), data)
Board.print()