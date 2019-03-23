import json, urllib.request, requests
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls = 45, period = 120) 
def get_each_rank(sum_id,key):
    player_URL = "https://na1.api.riotgames.com/lol/league/v4/positions/by-summoner/"+str(sum_id)+"?api_key="+key
    try:   
        player_data = requests.get(player_URL).json()
        return player_data[0]['tier']
    except:
        return "Player Not Ranked"
