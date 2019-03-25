'''
1. get matches, rank of first player, and game length, get about 1000 matches per tier (excluding master+)
2. get array of every tier
'''

import jsonData, getplayerrank,json, averagegamelength

def main():
    key = "RGAPI-57c2caae-4e3c-4e10-87c5-d8ab112a69e7"
    #starting point: 2996181980
    range_start = 2950608847
    range_end = 3004647440
    json_list = [] #this list will have a list of all the dictionaries. Each index contains info about a match (rank, patch, game length)
    for x in range(range_start,range_end,10000): #you can change the step. but if you leave it at 10000 you can just increase range_start by 
        #1 and it'll go through thousands of new ID's. 
        append_item = jsonData.find_matches(x,key)
        if append_item != None:
            json_list.append(append_item)
    final_list = {'matches':None}
    final_list.update({'matches':json_list})
    with open('availablematches.json','w') as data:
        json.dump(final_list, data, indent= True) #final_list has all the matches, add this to the json.
    #this gets you the list of matches you can test over...
    #iterate through the json to get the matchIds, game duration, rank
    patches = ['9.1','9.2','9.3','9.4','9.5','9.6'] #you can change this value
    averagegamelength.patch_list(patches) #creates a new json file and uploades average game length.
    print("Matches have been analyzed")




if __name__ == '__main__':
    main()