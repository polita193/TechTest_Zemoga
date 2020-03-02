from selenium.webdriver.common.by import By
from pages.page import Page


class ItineraryPage(Page):
    # LOCATORS
    _number_of_days = (By.CLASS_NAME, "duration-title")
    _itinerary_by_day = (By.CLASS_NAME, "vrg-search-unit")
    _book_now_button = (By.ID, "sm-booking-btn")

    def __init__(self, context):
        Page.__init__(self, context)

    def is_book_now_button_displayed(self):
        return self.is_element_displayed(self._book_now_button)

    def is_itinerary_by_day_displayed(self):
        #to do...
        return True