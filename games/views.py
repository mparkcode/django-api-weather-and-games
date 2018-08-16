from django.shortcuts import render
import requests
from igdb_api_python.igdb import igdb
import os
from datetime import datetime
# Create your views here.
def get_games(request):
    r = igdb(os.environ.get("igdb_api_key"))
    games=[]
    # result=r.games(3192)
    
    
    result = r.games({
        'search': "final fantasy",
        'fields' : ['name','summary', 'rating', 'url', 'screenshots', 'cover', 'first_release_date']
    })
    
    for game in result.body:
        if 'first_release_date' in game:
            game['first_release_date'] = datetime.utcfromtimestamp(int(game['first_release_date'] / 1000)).strftime('%Y/%m/%d')
        games.append(game)
    return render(request, "games/get_games.html", {'games':games})