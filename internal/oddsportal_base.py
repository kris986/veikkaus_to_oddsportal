from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class OddsportalBase:

    def collect_data_by_dict(self, driver, data_dict):
        for event_title in data_dict:
            self.try_searching(driver, event_title)
            self.go_to_search_result_page(driver)
            self.collect_bookmaker(driver, bookmaker_name)

    def try_searching(self, driver, phrase):
        try:
            self.wait_visibility_css_selector('div#search-box')
            search_field = driver.find_element_by_css_selector('input#search')
            search_field.send_key(phrase)
            
        except TimeoutException as e:
            print(e.msg)




    def go_to_search_result_page(self, driver):
        pass

    def wait_visibility_css_selector(self, driver, element, timeout=20):
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def collect_bookmaker(self, driver, bookmaker_name):
        pass
        
