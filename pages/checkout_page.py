"""Page objects for the three checkout steps."""
import re

from pages.base_page import BasePage


def _money(text: str) -> float:
    return float(re.search(r"\d+\.\d{2}", text).group())


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Step one: your information
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.error = page.locator('[data-test="error"]')
        # Step two: overview
        self.item_prices = page.locator('[data-test="inventory-item-price"]')
        self.subtotal = page.locator('[data-test="subtotal-label"]')
        self.tax = page.locator('[data-test="tax-label"]')
        self.total = page.locator('[data-test="total-label"]')
        self.finish_button = page.locator('[data-test="finish"]')
        # Step three: complete
        self.complete_header = page.locator('[data-test="complete-header"]')

    def fill_information(self, first: str, last: str, postal: str) -> None:
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_button.click()

    def item_total(self) -> float:
        return round(sum(_money(p) for p in self.item_prices.all_inner_texts()), 2)

    def subtotal_value(self) -> float:
        return _money(self.subtotal.inner_text())

    def tax_value(self) -> float:
        return _money(self.tax.inner_text())

    def total_value(self) -> float:
        return _money(self.total.inner_text())

    def finish(self) -> None:
        self.finish_button.click()
