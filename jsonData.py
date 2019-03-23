import json, urllib.request, requests, getplayerrank
from ratelimit import limits, sleep_and_retry

#Riot api only allows for 100 calls every two minutes... since we have two functions calling api for every match,
#we should only allow each one to have less than 50 every two minutes. Using 45 just to be safe.
@sleep_and_retry
@limits(calls = 45, period = 120) 
def find_matches(x,key):
        match_list = {}
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
                        print('match analyzed')
                        return match_list                
        except:
                print("match doesn\'t exist")

