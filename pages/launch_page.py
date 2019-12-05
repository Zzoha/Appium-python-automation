from pages.base_page import Page
from selenium.webdriver.common.by import By


class LaunchPage(Page):
    SEARCH = (By.ID, 'org.wikipedia:id/search_container')

    def tap_search(self):
        self.click(*self.SEARCH)
