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

DRIVER_ROOT = os.path.abspath(os.path.join(__file__, "../../chromedriver/chromedriver"))

driver = webdriver.Chrome(DRIVER_ROOT)
driver.get('https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc')

def load_more():
    run = True

    while run:
        try:
            print('this is running something')
            load_more_bttn = driver.find_element_by_link_text('Show More')
            time.sleep(2)
            load_more_bttn.click()
            time.sleep(5)
        except Exception as e:
            print(e)
            break
    page_source = driver.page_source
    get_players(page_source)
    time.sleep(10)
    driver.quit()

def get_players(page_source):
    # espn_html = bs(page_source, 'html.parser')
    # return espn_html
    print(page_source)

# def get_names():
#     espn_html = get_players()
#     player_tag = espn_html.select('div > a')
#     for names in player_tag:
#         names = names.get_text()
#         print(names)

if __name__ == "__main__":
    load_more()