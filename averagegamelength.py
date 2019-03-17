import json

def getAverageLength(patch_num):
    count = 0
    total = 0
    with open('availablematches', 'r') as data:
        for x in data['matches']:
            if data['matches']['patch'] == patch_num:
                count += 1
                total += data['matches']['gameDuration']
    game_length = total/count
    minutes = str(game_length//60)
    seconds = str(game_length%60).zfill(2)
    final_log = {}
    final_log['patch'] = patch_num
    final_log['game_length'] = f"{minutes}:{seconds}" 
