import requests
from bs4 import BeautifulSoup as bs

def get_html():
    url = 'https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc'
    response = requests.get(url)
    espn_html = bs(response.text, 'html.parser')
    return espn_html

def get_names():
    espn_html = get_html()
    player_tag = espn_html.select('div > a')
    for names in player_tag:
        names = names.get_text()

get_names()