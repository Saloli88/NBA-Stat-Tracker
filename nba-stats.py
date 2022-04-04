from ast import Lambda

from re import X
from turtle import home
from unicodedata import name
from requests import get


BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"


data = get(BASE_URL+ALL_JSON).json()
def get_links():
    links = data['links']
    return links

def get_scoreBoard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']
    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        print("-----------------------------------")
        print(f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        break

def get_leaderboard():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']
    teams = list( filter(lambda x: x['name']!="Teams",teams))
    teams.sort(key= lambda x : (x['ppg']['rank']))

    for team in teams:
        name = team['name']
        avg = team['ppg']['avg']
        print(f"{name}-{avg}")

def menu():
    loop = True
    while loop:
        choose = int(input('1-Get current scoreboard \n2-Get Leaderboard \n3-Exit \n'))
        if (choose==1):
            get_scoreBoard()
        elif (choose==2):
            get_leaderboard()
        elif (choose==3):
            loop = False
        else:
                continue
        
menu()