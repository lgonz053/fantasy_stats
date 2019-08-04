import requests
from bs4 import BeautifulSoup as bs

def get_data():
    url = 'https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc'
    response = requests.get(url)
    espn_data = bs(response.text, 'html.parser')

    return espn_data