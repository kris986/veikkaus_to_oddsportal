import urllib
from time import sleep

from selenium import webdriver
from external.veikkaus_base import VeikkausBase
from internal.oddsportal_base import OddsportalBase
from .build_xlsx import write_to_excel

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
    go_to_url(driver, veikkaus_url)
    data_dict = veikkaus_base.collect_tennis_data(driver)
#     data_dict = {
#   'R.Nadal - N.Basilashvili': [
#     {
#       'veikkaus': {
#         'odds_1': '1,04',
#         'odds_2': '8,40'
#       }
#     }
#   ],
#   'D.Kuzmanov - A.Cozbinov': [
#     {
#       'veikkaus': {
#         'odds_1': '1,07',
#         'odds_2': '7,00'
#       }
#     }
#   ],
#   'F.Fognini - Ca.Ruud': [
#     {
#       'veikkaus': {
#         'odds_1': '1,38',
#         'odds_2': '2,80'
#       }
#     }
#   ],
#   'S.Darcis - C.Norrie': [
#     {
#       'veikkaus': {
#         'odds_1': '2,95',
#         'odds_2': '1,35'
#       }
#     }
#   ],
#   'D.Medvedev - J.Isner': [
#     {
#       'veikkaus': {
#         'odds_1': '1,27',
#         'odds_2': '3,45'
#       }
#     }
#   ]
# }
    go_to_url(driver, oddsportal_url)
    data_dict = oddssportal_base.collect_data_by_dict(driver, data_dict)
    write_to_excel(data_dict)
    driver.close()
