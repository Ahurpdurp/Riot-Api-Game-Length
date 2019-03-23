'''
1. get matches, rank of first player, and game length, get about 1000 matches per tier (excluding master+)
2. get array of every tier
'''

import jsonData, getplayerrank,json, averagegamelength

def main():
    key = "RGAPI-0281e8af-6f34-4bc1-95fc-df4d00221e30"
    #starting point: 2996181980
    range_start = 2956718845
    range_end = 3004647438
    json_list = [] #this list will have a list of all the dictionaries. Each index contains info about a match (rank, patch, game length)
    for x in range(range_start,2956718885):
        append_item = jsonData.find_matches(x,key)
        if append_item != None:
            json_list.append(append_item)
    final_list = {'matches':None}
    final_list.update({'matches':json_list})
    with open('availablematches.json','w') as data:
        json.dump(final_list, data, indent= True) #final_list has all the matches, add this to the json.
    #this gets you the list of matches you can test over...
    #iterate through the json to get the matchIds, game duration, rank
    averagegamelength.main() #creates a new json file and uploades average game length.
    print("Matches have been analyzed")




if __name__ == '__main__':
    main()