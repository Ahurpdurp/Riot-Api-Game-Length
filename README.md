# Riot-Api-Game-Length
Simple script to gather data from the Riot API and calculate the average duration of League of Legends games from different patches

I'm currently testing out using the RIOT API for fun. This script (currently work in progress) extracts data from the most recent patches and calculate the average length of a legaue of legends match, separated by divison as well. 


Make sure to change the "key" variable to whatever your api key currently is. The one in the file is expired. Currently, patches 9.1 through 9.6 are analyzed. You can add patch numbers to the patches list to change the scope. Make sure to change the "range_end" variable so that it analyzes more games (ex. if patch 9.7 is added, test that the new range_end actually analyzes matches in patch 9.7). I'm not sure exactly how riot determines game_id, but higher game_id's will get more recent matches (ex. An ID of 3004647438 is a match played in patch 9.6, but a higher ID may represent a match played in a more recent patch). 

The Json files you see contain all the extracted data. The current things are just examples. Ideally, we'd want more than 100,000 matches for a good sample size. Keep in the mind the json files I uploaded to github have a couple of hundred items, because that's how much I extract at a time. 

The script will extract data from a specific range, and also display the statistics for that range. Make sure to store the data if you want to run the script multiple times for different ranges. I personally just converted the json file to an excel and I have a big excel sheet. On the second tab of the excel sheet I calculate the game length using built in excel functions - by doing it this way, every time I add new entries it'll automatically calculate whatever I want it to. 
