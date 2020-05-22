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

# def pull_data():
#     espn_html = load_more_data()
#     player_data = get_player_data(espn_html)

def load_more_data():
    driver.get(
        "https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc"
    )
    while True:
        try:
            load_more_bttn = driver.find_element_by_link_text("Show More")
            load_more_bttn.click()
            print("Loading data...")
            time.sleep(3)
        except Exception as e:
            print(e)
            break
    time.sleep(10)
    parsed_html = bs(driver.page_source, "html.parser")
    driver.quit()
    get_player_data(parsed_html)
    # get_headers(parsed_html)
    print("Data pull complete!")

def get_headers(espn_html):
    headers_tag = espn_html.select("thead > tr > th > span")
    headers = []
    for tag in headers_tag:
        try:
            if tag["title"] is not "":
                headers.append(tag["title"])
        except:
            continue
    return headers

def get_player_data(espn_html):
    players_data = espn_html.select("td > div > a")
    players = {}
    idx = 0
    for player in players_data:
        name = player.get_text()
        if name not in players.keys():
            players[name] = idx
        idx += 1
    return players

if __name__ == "__main__":
    load_more_data()
