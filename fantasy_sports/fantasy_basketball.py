import os
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
    print("Complete!")
    time.sleep(10)
    parsed_html = bs(driver.page_source, "html.parser")
    get_names(parsed_html)
    driver.quit()

def get_names(espn_html):
    player_tag = espn_html.select('div > a')
    for names in player_tag:
        names = names.get_text()
        print(names)

if __name__ == "__main__":
    load_more_data()
