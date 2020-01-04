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
            details = soup.find('div', {'class': 'event-row'})
            for detail in details:
                source_list = list()
                dtls_dict = dict()
                checker_class = detail.get_attribute_list('class')
                if 'event-info' in checker_class:
                    event_title = detail.find('span', {'class': 'event-title'}).text
                    event_number = detail.find('span', {'class': 'event-number'}).text
                    # tennis_dict[event_number] = game_dict
                    # dtls_dict
                    game_dict[event_title] = source_list

                elif 'event-outcome-holder' in checker_class:
                    odd_dict = dict()
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
        print(game_dict)
