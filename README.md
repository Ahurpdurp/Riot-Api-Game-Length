# Riot-Api-Game-Length
Simple script to gather data from the Riot API and calculate the average duration of League of Legends games from different patches

I'm currently testing out using the RIOT API for fun. This script (currently work in progress) extracts data from the most recent patches and calculate the average length of a legaue of legends match, separated by divison as well. 


Make sure to change the "key" variable to whatever your api key currently is. The one in the file is expired. Currently, patches 9.1 through 9.6 are analyzed. You can add patch numbers to the patches list to change the scope. Make sure to change the "range_end" variable so that it analyzes more games (ex. if patch 9.7 is added, test that the new range_end actually analyzes matches in patch 9.7). 
