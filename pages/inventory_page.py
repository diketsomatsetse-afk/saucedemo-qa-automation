"""Page object for the product listing (inventory) screen."""
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator('[data-test="title"]')
        self.items = page.locator('[data-test="inventory-item"]')
        self.item_names = page.locator('[data-test="inventory-item-name"]')
        self.item_prices = page.locator('[data-test="inventory-item-price"]')
        self.item_images = page.locator(".inventory_item_img img")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def prices(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.item_prices.all_inner_texts()]

    def sort_by(self, option_value: str) -> None:
        """option_value: 'az', 'za', 'lohi' or 'hilo'."""
        self.sort_dropdown.select_option(option_value)

    def add_to_cart(self, product_name: str) -> None:
        item = self.items.filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self, product_name: str) -> None:
        item = self.items.filter(has_text=product_name)
        item.get_by_role("button", name="Remove").click()

    def open_cart(self) -> None:
        self.cart_link.click()
