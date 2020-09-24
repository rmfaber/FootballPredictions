import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

def start_browser(url='https://www.voetbal.com/'):
    browser = webdriver.Chrome()
    browser.get(url)
    # agree to use cookies
    time.sleep(2)
    browser.find_element_by_css_selector('button[mode="primary"]').click()
    return browser

def get_teamslist_games(browser,season,roundnr):
    """Get all the games for a given season and roundnr
    
    Parameters
    -------------
    browser, Selenium browserobject
    
    season, str
        String with format: {firstyear}-{secondyear}
    
    roundnr, str
        String of the roundnr (digit between 1 and 34)"""
    url = f"https://www.voetbal.com/wedstrijdgegevens/ned-eredivisie-{season}-spieltag/{roundnr}/"
    browser.get(url)
    data = requests.get(browser.current_url)
    soup = BeautifulSoup(data.text,'html.parser')
    games = soup.select("a[title*=Wedstrijddetails]")
    table = soup.findAll('table', { 'class' : 'standard_tabelle' })
    teams = table[1].select("a[href*=teams]")
    teams
    teamslist = []
    for team in teams:
        teamslist.append(team.get_text())
    return teamslist, games


def get_teamslist(soup):
    """Find all teams that participate in this year of the Eredivisie"""
    table = soup.findAll('table', { 'class' : 'standard_tabelle' })
    teams = table[1].select("a[href*=teams]")
    teams
    teamslist = []
    for team in teams:
        teamslist.append(team.get_text())
    return(teamslist)
    
def team_identification(game,teamslist):
    """Identify the home and awayteams of a game"""
    for team in teamslist:
        if team in game['title'].split(' -')[0]:
            hometeam = team
        elif team in game['title'].split(' -')[1]:
            awayteam = team
    return hometeam,awayteam
    
def goals(game):
    """Identify the goals scored and the result of the game"""
    goals_scored = game.get_text().split()[0]
    homegoals = goals_scored.split(':')[0]
    awaygoals = goals_scored.split(':')[1]
    if homegoals>awaygoals:
        return([homegoals,awaygoals,1])
    elif awaygoals>homegoals:
        return([homegoals,awaygoals,2])
    else:
        return([homegoals,awaygoals,3])
    
def gamestats(game, teamslist):
    """Combine the team identification and result"""
    hometeam, awayteam = team_identification(game, teamslist)
    resultlist = goals(game)
    homegoals = resultlist[0]
    awaygoals = resultlist[1]
    result = resultlist[2]
    if result == 1:
        homepoints = 3
        awaypoints = 0
    elif result == 2:
        homepoints = 0
        awaypoints = 3
    else:
        homepoints = 1
        awaypoints = 1
    return({"Home":hometeam,"Away":awayteam,"HomeGoals":homegoals,"AwayGoals":awaygoals,"Result":result,
            "HomePoints":homepoints,"AwayPoints":awaypoints})

def create_df(browser,columns,roundnrs,startjaar,eindjaar):
    df = pd.DataFrame(columns=columns)
    jaar = startjaar
    while jaar <= eindjaar:
        season = f"{jaar}-{jaar+1}"
        for roundnr in roundnrs:
            teamslist, games = get_teamslist_games(browser,season=season,roundnr=str(roundnr))
            for game in games:
                resultdict = gamestats(game,teamslist)
                resultdict["Season"] = season
                resultdict["Round"] = roundnr
                df = df.append(resultdict,ignore_index=True)
        jaar+=1
    return df

def test(a,b):
    return a + b