#!/usr/bin/env python3
import urllib
from time import sleep

from selenium import webdriver
from external.veikkaus_base import VeikkausBase
from internal.oddsportal_base import OddsportalBase
from build_xlsx import write_to_excel

veikkaus_base = VeikkausBase()
oddssportal_base = OddsportalBase()


def run_driver():
    driver = webdriver.Chrome()
    return driver


def go_to_url(driver, page_url, pref_url=''):
    url = urllib.parse.urljoin(page_url, pref_url)
    driver.get(url)
    sleep(2)
    return driver


if __name__ == "__main__":
    veikkaus_url = 'https://www.veikkaus.fi/fi/pitkaveto?sportId=10&selectedLeagues=10-all'
    oddsportal_url = "https://www.oddsportal.com"
    driver = run_driver()
    try:
        go_to_url(driver, veikkaus_url)
        data_dict = veikkaus_base.collect_tennis_data(driver)
        go_to_url(driver, oddsportal_url)
        data_dict = oddssportal_base.collect_data_by_dict(driver, data_dict)
        write_to_excel(data_dict)
    except Exception as e:
        print(e)
    finally:
        driver.close()
        quit()
