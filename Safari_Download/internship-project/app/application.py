from pages.base_page import Page
from pages.main_page import MainPage
from pages.header import Header


class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)