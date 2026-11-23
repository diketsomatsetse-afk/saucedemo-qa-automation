"""End-to-end checkout flow and form validation."""
import pytest
from playwright.sync_api import expect

from conftest import PASSWORD, PROBLEM_USER
from pages.inventory_page import InventoryPage

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"
TAX_RATE = 0.08  # SauceDemo charges 8% tax


def _go_to_checkout(inventory, cart_page, *products):
    for product in products:
        inventory.add_to_cart(product)
    inventory.open_cart()
    cart_page.checkout()


@pytest.mark.smoke
def test_complete_purchase(logged_in, cart_page, checkout_page):
    _go_to_checkout(logged_in, cart_page, BACKPACK)
    checkout_page.fill_information("Test", "User", "2000")
    checkout_page.finish()
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")


def test_order_totals_are_correct(logged_in, cart_page, checkout_page):
    _go_to_checkout(logged_in, cart_page, BACKPACK, BIKE_LIGHT)
    checkout_page.fill_information("Test", "User", "2000")

    item_total = checkout_page.item_total()
    assert checkout_page.subtotal_value() == item_total
    assert checkout_page.tax_value() == round(item_total * TAX_RATE, 2)
    assert checkout_page.total_value() == round(item_total + checkout_page.tax_value(), 2)


@pytest.mark.parametrize(
    "first, last, postal, message",
    [
        ("", "User", "2000", "First Name is required"),
        ("Test", "", "2000", "Last Name is required"),
        ("Test", "User", "", "Postal Code is required"),
    ],
    ids=["missing-first-name", "missing-last-name", "missing-postal-code"],
)
def test_checkout_form_validation(logged_in, cart_page, checkout_page, first, last, postal, message):
    _go_to_checkout(logged_in, cart_page, BACKPACK)
    checkout_page.fill_information(first, last, postal)
    expect(checkout_page.error).to_contain_text(message)


@pytest.mark.xfail(reason="BUG-002: problem_user cannot type in the Last Name field", strict=True)
def test_problem_user_can_enter_last_name(login_page, page, cart_page, checkout_page):
    login_page.login(PROBLEM_USER, PASSWORD)
    _go_to_checkout(InventoryPage(page), cart_page, BACKPACK)
    checkout_page.last_name.fill("User")
    expect(checkout_page.last_name).to_have_value("User", timeout=2000)
