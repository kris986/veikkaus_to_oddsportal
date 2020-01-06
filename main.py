#!/usr/bin/env python3
import urllib
from time import sleep
from xvfbwrapper import Xvfb

from selenium import webdriver
from external.veikkaus_base import VeikkausBase
from internal.oddsportal_base import OddsportalBase
from build_xlsx import write_to_excel
from selenium.webdriver.chrome.options import Options

veikkaus_base = VeikkausBase()
oddssportal_base = OddsportalBase()
vdisplay = Xvfb()


def run_driver():
    # version for Windows
    # driver = webdriver.Chrome()
    # version for Linux
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)
    return driver


def go_to_url(driver, page_url, pref_url=''):
    url = urllib.parse.urljoin(page_url, pref_url)
    print('Driver run')
    driver.get(url)
    sleep(2)
    return driver


if __name__ == "__main__":
    vdisplay.start()
    veikkaus_url = 'https://www.veikkaus.fi/fi/pitkaveto?sportId=10&selectedLeagues=10-all'
    oddsportal_url = "https://www.oddsportal.com"
    driver = run_driver()
    try:
        go_to_url(driver, veikkaus_url)
        print('Started collect data on veikkaus...')
        data_dict = veikkaus_base.collect_tennis_data(driver)
        print('Ended collect data on veikkaus')
        go_to_url(driver, oddsportal_url)
        print('Started collect data on oddsportal...')
        data_dict = oddssportal_base.collect_data_by_dict(driver, data_dict)
        print('Ended collect data on oddsportal')
        print('Creating excel file')
        write_to_excel(data_dict)
        print('Parsing is finished')
    except Exception as e:
        print(e)
    finally:
        driver.close()
        vdisplay.stop()
        quit()
