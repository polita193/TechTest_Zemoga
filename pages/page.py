from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):

    def __init__(self, context, base_url='http://www.google.com'):
        self.driver = context.driver
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, loc):
        self.wait_for_element(loc)
        return self.driver.find_element(*loc)

    def get_elements_list_by_selector(self, loc):
        self.wait_for_element(loc)
        return self.driver.find_elements(*loc)

    def click_element_from_list(self, selection_value, loc):
        options_list = self.get_elements_list_by_selector(loc)
        for element in options_list:
            if element.text == selection_value:
                element.click()
                break

    def go(self, url):
        self.driver.get(url)

    def scroll_to_element(self, loc):
        ActionChains(self.driver).move_to_element(self.find_element(loc)).perform()

    def wait_for_element(self, loc):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc))
        except(TimeoutException, NoSuchElementException, ElementNotVisibleException):
            return False

    def is_element_displayed(self, loc):
        try:
            return self.find_element(loc).is_displayed()
        except(TimeoutException, NoSuchElementException, ElementNotVisibleException):
            return False

    def scroll_down(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


