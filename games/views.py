from django.shortcuts import render
import requests
# Create your views here.
def get_games(request):
    return render(request, "games/get_games.html")