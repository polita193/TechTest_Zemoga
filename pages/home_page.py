from selenium.webdriver.common.by import By
from pages.page import Page


class HomePage(Page):
    # LOCATORS
    _modal_ad = (By.CLASS_NAME, "vifp-sweeps-modal")
    _close_ad = (By.CLASS_NAME, "vifp-no")
    _popup_bar = (By.CLASS_NAME, "popUpRmktBB")
    _close_popup_bar = (By.ID, "closeRmkt")
    _sail_to = (By.ID, "cdc-destinations")
    _duration = (By.ID, "cdc-durations")
    _options_list = (By.CLASS_NAME, "cdc-filter-button")
    _filter_by_price = (By.CLASS_NAME, "sfn-nav__item-pricing")
    _slider = (By.CSS_SELECTOR, ".filter-price .sfp-slider")
    _result_grid =(By.CLASS_NAME, "ccs-search-results")
    _results_grid_items = (By.CLASS_NAME, "vrg-result-item")

    def __init__(self, context):
        Page.__init__(self, context)

    def search_cruise(self, sail_to, duration):
        self.close_ad()
        self.scroll_to_element(self._sail_to)
        self.find_element(self._sail_to).click()
        self.click_element_from_list(sail_to, self._options_list)
        self.find_element(self._duration).click()
        self.click_element_from_list(duration, self._options_list)

    def results_grid_is_displayed(self):
        return self.is_element_displayed(self._result_grid)

    def check_filter_by_price(self):
        self.find_element(self._filter_by_price).click()
        return self.is_element_displayed(self._slider)

    def close_ad(self):
        if self.is_element_displayed(self._modal_ad):
            self.find_element(self._close_ad).click()
        if self.is_element_displayed(self._popup_bar):
            self.find_element(self._close_popup_bar).click()
