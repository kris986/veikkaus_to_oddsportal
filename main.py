#!/usr/bin/env python3
import logging
import urllib
from pprint import pprint
from time import sleep
from xvfbwrapper import Xvfb
import sentry_sdk
from sentry_sdk import capture_exception

from selenium import webdriver
from external.veikkaus_base import VeikkausBase
from internal.oddsportal_base import OddsportalBase
from selenium.webdriver.chrome.options import Options

from post_to_xlsx import update_xlsl_file, analyze_existing_matches

log = logging.getLogger(__name__)

veikkaus_base = VeikkausBase()
oddssportal_base = OddsportalBase()
sentry_sdk.init("https://61b92881c93b447aacba6df4ba5690dc@sentry.io/2097752")


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
#     # init driver with options if script will run on Win Corporate version or Pro
#     options = webdriver.ChromeOptions()
#     options.add_argument('--disable-features=RendererCodeIntegrity')
#     driver = webdriver.Chrome(options=options)

    # driver = webdriver.Chrome()
    # return driver


def go_to_url(driver, page_url, pref_url=''):
    url = urllib.parse.urljoin(page_url, pref_url)
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
        pprint(data_dict)
        sleep(5)
        print('Ended collect data on veikkaus')
        go_to_url(driver, oddsportal_url)
        print('Started collect data on oddsportal...')
        data_dict = oddssportal_base.collect_data_by_dict(driver, data_dict)
        print('Ended collect data on oddsportal')
        print('Creating excel file')
        update_xlsl_file(data_dict)
        print('Parsing is finished')
        print('Analyzing excl file')
        # analyzing existing matches and collecting match results
        analyze_existing_matches(driver)
        print('Ended analyze excl file')
    except Exception as e:
        capture_exception(e)
        log.exception('Это сообщение об ошибке:')
    finally:
        driver.close()
        vdisplay.stop()
        quit()
