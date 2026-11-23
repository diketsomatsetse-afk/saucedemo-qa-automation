"""Adding and removing items in the cart."""
import pytest
from playwright.sync_api import expect

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"


@pytest.mark.smoke
def test_add_item_updates_badge_and_cart(logged_in, cart_page):
    logged_in.add_to_cart(BACKPACK)
    expect(logged_in.cart_badge).to_have_text("1")

    logged_in.open_cart()
    assert cart_page.names() == [BACKPACK]


def test_add_two_items(logged_in, cart_page):
    logged_in.add_to_cart(BACKPACK)
    logged_in.add_to_cart(BIKE_LIGHT)
    expect(logged_in.cart_badge).to_have_text("2")

    logged_in.open_cart()
    assert sorted(cart_page.names()) == sorted([BACKPACK, BIKE_LIGHT])


def test_remove_item_clears_badge(logged_in):
    logged_in.add_to_cart(BACKPACK)
    logged_in.remove_from_cart(BACKPACK)
    expect(logged_in.cart_badge).to_have_count(0)


def test_cart_persists_after_reload(logged_in, page):
    logged_in.add_to_cart(BACKPACK)
    page.reload()
    expect(logged_in.cart_badge).to_have_text("1")
