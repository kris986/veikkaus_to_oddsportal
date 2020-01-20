from time import sleep
import re

from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class OddsportalBase:

    def collect_data_by_dict(self, driver, data_dict):
        chkr = 1
        for event_title in data_dict:
            print(f'Handling {chkr} from {len(data_dict)}\nCollecting event {event_title}')
            if self.try_searching(driver, event_title):
                if self.handling_search_results_page(driver, event_title):
                    time_dict = dict()
                    time = driver.find_element_by_css_selector('div#col-content p.date').text
                    time = re.sub(r'^[a-zA-Z]*,\s', '', time)
                    time_dict['time'] = time
                    data_dict[event_title].append(time_dict)
                    bet365 = self.collect_bookmaker(driver, 'bet365')
                    data_dict[event_title].append(bet365)
                    william_hill = self.collect_bookmaker(driver, 'William Hill')
                    data_dict[event_title].append(william_hill)
                    onexbet = self.collect_bookmaker(driver, '1xBet')
                    data_dict[event_title].append(onexbet)
                    pinnacle = self.collect_bookmaker(driver, 'Pinnacle')
                    data_dict[event_title].append(pinnacle)
            chkr += 1
        return data_dict

    def try_searching(self, driver, phrase):
        try:
            self.wait_visibility_css_selector(driver, 'div#search-box')
            search_field = driver.find_element_by_css_selector('input#search')
            search_field.send_keys(phrase)
            driver.find_element_by_css_selector('a#search-submit').click()
            sleep(2)
            self.wait_visibility_css_selector(driver, 'div.spc.filterOpts')
            return True
        except TimeoutException:
            driver.refresh()
            return False
        except NoSuchElementException:
            return False

    def handling_search_results_page(self, driver, search_phrase):
        try:
            result_phrase = driver.find_elements_by_css_selector('td.name a')
            for a in result_phrase:
                if '/tennis/' in a.get_attribute('href'):
                    if self.compare_phrase_and_results(search_phrase, a.text):
                        a.click()
                        self.wait_visibility_css_selector(driver, 'div#tab-nav-main')
                        return driver

            return False
        except TimeoutException:
            driver.refresh()
            return False
        except NoSuchElementException:
            return False

    def wait_visibility_css_selector(self, driver, element, timeout=20):
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def collect_bookmaker(self, driver, bookmaker_name):
        bookmaker_dict = dict()
        odd_dict = dict()
        bookmaker_dict[bookmaker_name] = odd_dict
        try:
            self.wait_visibility_css_selector(driver, ".table-container")
            action = ActionChains(driver)
            trs = driver.find_elements_by_css_selector('table.table-main tr.lo')
            for tr in trs:
                odd_dict = dict()
                checker = 1
                try:
                    bookmaker = tr.find_element_by_css_selector('.l a.name')
                    if bookmaker.text == bookmaker_name:
                        data = tr.find_elements_by_css_selector('td.right.odds')
                        for element in data:
                            col_item = element.text
                            odd_dict[f'col_{checker}'] = col_item
                            try:
                                action.move_to_element(element).perform()
                                coefficient = driver.find_element_by_id('tooltipdiv')
                                soup = BeautifulSoup(coefficient.get_attribute('innerHTML'), 'html.parser')
                                data = soup.findAll('strong')[-1].text
                                if data == 'Click to BET NOW':
                                    data = soup.findAll('strong')[-2].text
                                else:
                                    data = soup.findAll('strong')[-1].text
                                odd_dict[f'odds_{checker}'] = data
                            except Exception:
                                pass
                            bookmaker_dict[bookmaker_name] = odd_dict
                            checker += 1
                except (NoSuchElementException, ElementNotVisibleException):
                    pass
        except (NoSuchElementException, TimeoutException) as e:
            print(e.msg)
            pass
        finally:
            return bookmaker_dict

    def compare_phrase_and_results(self, search_phrase, result_phrase):
        search_phrase = search_phrase.replace('.', '. ').upper()
        result_phrase = result_phrase.upper()
        search_list = set(search_phrase.split(' '))
        result_list = set(result_phrase.split(' '))
        if len(result_list.symmetric_difference(search_list)) <= 1:
            return True
        else:
            return False

    def collect_result_of_match(self, driver):
        try:
            result = driver.find_element_by_css_selector('div#event-status p.result')
            result = re.sub(r'Final result ', '', result.get_attribute('innerHTML'))
            result = (result.replace('<sup>', '/')).replace('</sup>', '')
            soup = BeautifulSoup(result, 'html.parser')
            return soup.text
        except NoSuchElementException:
            return False

    def event_status(self, driver):
        try:
            started = 'started'
            status = driver.find_element_by_css_selector('div#event-status p.result-alert span')
            if status.text == 'The match has already started.':
                return started
        except NoSuchElementException:
            return False
