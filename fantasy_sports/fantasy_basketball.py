import os
import requests
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
driver.get('https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc')

def load_more():
    load_more_bttn = driver.find_element_by_class_name('loadMore__link')
    time.sleep(2)
    load_more_bttn.click()
    time.sleep(2)


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
        print(names)

load_more()