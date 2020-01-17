#!/usr/bin/env python3
import logging
import urllib
from time import sleep
from xvfbwrapper import Xvfb

from selenium import webdriver
from external.veikkaus_base import VeikkausBase
from internal.oddsportal_base import OddsportalBase
from selenium.webdriver.chrome.options import Options

from post_to_xlsx import update_xlsl_file

log = logging.getLogger(__name__)

veikkaus_base = VeikkausBase()
oddssportal_base = OddsportalBase()
vdisplay = Xvfb()


# version for Linux
def run_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver


# version for Windows
# def run_driver():
    # init driver with options if script will run on Win Corporate version or Pro
    # options = webdriver.ChromeOptions()
    # options.add_argument('--disable-features=RendererCodeIntegrity')
    # driver = webdriver.Chrome(options=options)

    # driver = webdriver.Chrome()
    # return driver


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
        # data_dict = {'A.Barty - D.Yastremska': [{'veikkaus': {'event_description': 'Adelaide, Australia, WTA', 'odds_1': '10,45', 'odds_2': '20,55'}}, {'time': '18 Jan 2020, 12:00'}, {'bet365': {'col_1': '10.44', 'odds_1': '1.44', 'col_2': '20.75', 'odds_2': '2.75'}}, {'William Hill': {'col_1': '1.50', 'odds_1': '1.50', 'col_2': '2.60', 'odds_2': '2.60'}}, {'1xBet': {'col_1': '10.54', 'odds_1': '1.57', 'col_2': '20.64', 'odds_2': '2.42'}}, {'Pinnacle': {'col_1': '1.54', 'odds_1': '1.49', 'col_2': '2.66', 'odds_2': '2.82'}}], 'Bougrat/Remy - Noel/Orpana': [{'veikkaus': {'event_description': 'Monastir, Tunisia, Nelinpeli', 'odds_1': '2,85', 'odds_2': '1,37'}}], 'B.Paire - U.Humbert': [{'veikkaus': {'event_description': 'Auckland, Uusi-Seelanti', 'odds_1': '1,98', 'odds_2': '1,75'}}, {'time': '18 Jan 2020, 02:30'}, {'bet365': {'col_1': '2.10', 'odds_1': '2.10', 'col_2': '1.72', 'odds_2': '1.72'}}, {'William Hill': {'col_1': '2.00', 'odds_1': '2.10', 'col_2': '1.80', 'odds_2': '1.73'}}, {'1xBet': {'col_1': '2.04', 'odds_1': '1.81', 'col_2': '1.86', 'odds_2': '2.01'}}, {'Pinnacle': {'col_1': '2.05', 'odds_1': '1.75', 'col_2': '1.86', 'odds_2': '2.20'}}], 'E.Rybakina - Shuai Zhang': [{'veikkaus': {'event_description': 'Hobart, Australia', 'odds_1': '2,18', 'odds_2': '1,60'}}], 'L.Harris - A.Rublev': [{'veikkaus': {'event_description': 'Adelaide, Australia, ATP', 'odds_1': '3,55', 'odds_2': '1,25'}}], 'ATP  Australian Open': [{'veikkaus': {'event_description': 'ATP', 'odds_1': ' - ', 'odds_2': ' - '}}], 'WTA  Australian Open': [{'veikkaus': {'event_description': 'WTA', 'odds_1': ' - ', 'odds_2': ' - '}}]}
        print('Creating excel file')
        update_xlsl_file(data_dict)
        print('Parsing is finished')
    except Exception as inst:
        log.exception('Это сообщение об ошибке:')
    finally:
        driver.close()
        vdisplay.stop()
        quit()
