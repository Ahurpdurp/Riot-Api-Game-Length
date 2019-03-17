import json, urllib.request, requests, getplayerrank
from ratelimit import limits  

two_minutes = 120

@limits(calls = 90, period = two_minutes)
def find_matches(range_start,length,key):
        match_list = {}
        json_list = []
        for x in range(range_start,range_start+length):
                try:
                        URL = "https://na1.api.riotgames.com/lol/match/v4/matches/"+str(x)+"?api_key="+key
                        response = requests.get(URL).json()
                        if response['queueId'] == 420:
                                match_list['match'] = response['gameId']
                                match_list['gameDuration'] = response['gameDuration']
                                match_list['patch'] = response['gameVersion'].split('.')[0] + "." + response['gameVersion'].split('.')[1] 
                                for y in range(0,10): # starting from the first player...if he/she isn't ranked, then it moves to the next one)
                                    match_id = response['participantIdentities'][y]['player']['summonerId']
                                    match_list['rank'] = getplayerrank.get_each_rank(match_id,key)
                                    if match_list['rank'] != "Player Not Ranked":
                                        break

                                json_list.append(match_list.copy())
                                print('match analyzed')
                except:
                        print("code broke")
        final_list = {'matches':None}
        final_list.update({'matches':json_list})
        with open('availablematches.json','w') as data:
                json.dump(final_list, data, indent= True)

        print('done')
