import json

def getAverageLength(patch_num):

    final_log = {}
    final_log['patch'] = patch_num
    final_log['ranks'] = []
    temp_log = {} #for each rank, put the info into here. Then append this to final_log['ranks']
    ranks = ['IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','MASTER','CHALLENGER']
    with open('availablematches.json', 'r') as data_json:
        data = json.load(data_json)
        for rank in ranks:
            count = 0
            total = 0 #count and total reset for each rank to calculate average of each rank.
            for x in data['matches']:
                if x['patch'] == patch_num and x['rank'] == rank:
                    count += 1
                    total += x['gameDuration']
            if count > 0: #certain divisions (aka challenger) might not a single game that was analyzed. need to check if that's the case
                game_length = round(total/count)
                minutes = str(game_length//60)
                seconds = str(game_length%60).zfill(2)
                temp_log['rank'] = rank
                temp_log['game_length'] = f"{minutes}:{seconds}" 
                temp_log['games_analyzed'] = count
                final_log['ranks'].append(temp_log.copy())
            else: 
                temp_log['rank'] = rank
                temp_log['game_length'] = "No Games Analyzed"
                temp_log['games_analyzed'] = 0
                final_log['ranks'].append(temp_log.copy())

    return final_log

def patch_list(patches):
    patch_log = {} #contains info for each patch
    patch_log['patches'] = []
    for x in patches:
        patch_log['patches'].append(getAverageLength(x))
    with open('patchlog.json','w') as data:
        json.dump(patch_log, data, indent= True) #final_list has all the matches, add this to the json.


