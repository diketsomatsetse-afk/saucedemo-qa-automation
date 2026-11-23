"""Shared base class for all page objects."""
from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com"


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, path: str = "/") -> None:
        self.page.goto(BASE_URL + path)
