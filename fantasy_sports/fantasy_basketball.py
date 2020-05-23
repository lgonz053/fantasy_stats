import os
import re
import requests
import time
import webbrowser

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_ROOT = os.path.abspath(os.path.join(__file__, "../../chromedriver/chromedriver"))

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome(DRIVER_ROOT, chrome_options=options)

def pull_data():
    parsed_html = load_more_data()
    headers = get_headers(parsed_html)
    names = get_player_names(parsed_html)
    data = get_player_data(parsed_html)

def load_more_data():
    driver.get(
        "https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc"
    )
    while True:
        try:
            driver.find_element_by_link_text("Show More").click()
            print("Loading data...")
            time.sleep(3)
        except:
            time.sleep(10)
            break
    parsed_html = bs(driver.page_source, "html.parser")
    driver.quit()
    print("Data pull complete!")
    return parsed_html

def get_headers(html):
    headers_tag = html.select("thead > tr > th > span")
    headers = []
    for tag in headers_tag:
        try:
            if tag["title"] is not "":
                headers.append(tag["title"])
        except:
            continue
    return headers

def get_player_names(html):
    players_names = html.select("td > div > a")
    players = {}
    for idx, player in enumerate(players_names):
        name = player.get_text()
        if name not in players.keys():
            players[name] = idx
    return players

def get_player_data(html):
    player_data = html.select("tbody > tr")
    player_stats = {}
    for idx, player in enumerate(player_data):
        if idx not in player_stats.keys():
            data = []
            for stats in player:
                data.append(stats.get_text())
            player_stats[idx] = data
    return player_stats


if __name__ == "__main__":
    pull_data()
