from pprint import pprint
from time import sleep

from bs4 import BeautifulSoup


class VeikkausBase:

    def collect_tennis_data(self, driver):
        source_name = 'veikkaus'
        game_dict = dict()
        sleep(2)
        box = driver.find_elements_by_xpath(
            "//li[(contains(@class,'event-group-event')  and not(contains(@class, 'target-row')) and not(contains(@class, 'hidden')))]")
        for element in box:
            soup = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
            pprint(soup)
            sleep(5)
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
