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
    print("Data pull complete!")
    parsed_html = bs(driver.page_source, "html.parser")
    get_names(parsed_html)
    driver.quit()

def get_names(espn_html):
    count = 0
    player_row = espn_html.findAll("tr", {"class":"Table__TR Table__TR--sm Table__even"})
    print(player_row)
    # for player in player_row:
        # # if count < (len(player_row) / 2):
        # try:
        #     player_info = player.get_text()
        #     # regex - split at number and text, string to search
        #     name = re.match(r"([a-z]+)([0-9]+)", player_info, re.I).groups()
        #     print(name)
        # except:
        #     pass

if __name__ == "__main__":
    load_more_data()
