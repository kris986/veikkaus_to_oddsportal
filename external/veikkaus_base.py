from pprint import pprint
from time import sleep

from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from internal.oddsportal_base import OddsportalBase
from sentry_sdk import capture_exception


class VeikkausBase:
    odds_base = OddsportalBase()

    def collect_tennis_data(self, driver):
        source_name = 'veikkaus'
        game_dict = dict()
        box = self.collect_data_on_page(driver)
        if box:
            print(len(box))
            for element in box:
                print(element.text)
                soup = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
                details = soup.find('div', {'class': 'event-row'})
                odd_dict = dict()
                for detail in details:
                    source_list = list()
                    dtls_dict = dict()
                    # odd_dict = dict()
                    checker_class = detail.get_attribute_list('class')
                    if 'event-info' in checker_class:
                        event_title = detail.find('span', {'class': 'event-title'}).text
                        game_dict[event_title] = source_list

                        event_description = detail.find('span', {'class': 'event-description'}).text
                        odd_dict['event_description'] = event_description
                        dtls_dict[source_name] = odd_dict
                        source_list.append(dtls_dict)

                    elif 'event-outcome-holder' in checker_class:

                        if len(detail.find('div', {'class': 'events-details'}).contents) <= 1:
                            odds_1, odds_2 = ' - ', ' - '
                        else:
                            odds_1 = detail.find('button', {'data-outcome-id': '1'})
                            odds_1 = odds_1.find('span', {'class': 'odds'}).text
                            odds_2 = detail.find('button', {'data-outcome-id': '2'})
                            odds_2 = odds_2.find('span', {'class': 'odds'}).text
                        odd_dict['odds_1'] = odds_1
                        odd_dict['odds_2'] = odds_2
                        dtls_dict[source_name] = odd_dict
                        game_dict[event_title] = source_list
                        source_list.append(dtls_dict)
            # print(game_dict)
        return game_dict

    def collect_data_on_page(self, driver):
        try:
            # self.odds_base.wait_visibility_css_selector(driver, 'div#pitkaveto-sub-navigation-container', timeout=40)
            print('div#pitkaveto-sub-navigation-container EXISTS')
            box = driver.find_elements_by_xpath(
                "//li[(contains(@class,'event-group-event')  and not(contains(@class, 'target-row')) and not(contains(@class, 'hidden')))]")
            print('Boxes with data were founded')
            print(type(box))
            return box
        except(NoSuchElementException, TimeoutException) as e:
            capture_exception(e)
            return False
