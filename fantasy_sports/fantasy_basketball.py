import os
import requests
import time
import webbrowser

from bs4 import BeautifulSoup as bs
from selenium import webdriver      
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/leonardogonzalez/src/fantasy_stats/chromedriver/chromedriver')
driver.get('https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc')

def load_more():
    run = True

    while run:
        print('we are inside the while loop')
        try:
            print('this is running something')
            load_more_bttn = driver.find_element_by_link_text('Show More')
            time.sleep(2)
            load_more_bttn.click()
            time.sleep(5)
        except Exception as e:
            print(e)
            break
    print("Complete")
    time.sleep(10)
    driver.quit()

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