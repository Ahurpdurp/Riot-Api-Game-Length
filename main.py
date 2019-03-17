'''
1. get matches, rank of first player, and game length, get about 1000 matches per tier (excluding master+)
2. get array of every tier
'''

import jsonData, getplayerrank,json

def main():
    key = "RGAPI-fd6bea24-f345-4112-9893-3b6001542ed8"
    #starting point: 2996181980
    range_start = 2996181980
    range_end = 2996182480
    length = range_end - range_start
    jsonData.find_matches(range_start,length,key) #this gets you the list of matches you can test over...'''
    #iterate through the json to get the matchIds, game duration, rank





if __name__ == '__main__':
    main()