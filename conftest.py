"""Shared fixtures.

SauceDemo is a public practice site. The test accounts below are published
on its own login page for anyone to use, so they are safe to keep in code.
"""
import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"
STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PROBLEM_USER = "problem_user"


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def logged_in(login_page, page):
    """Log in as the standard user and return the inventory page."""
    login_page.login(STANDARD_USER, PASSWORD)
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
