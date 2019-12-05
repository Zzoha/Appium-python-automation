from pages.launch_page import LaunchPage
from pages.search_page import SearchPage


class Application:

    def __init__(self, driver):
        self.launch_page = LaunchPage(driver)
        self.search_page = SearchPage(driver)
