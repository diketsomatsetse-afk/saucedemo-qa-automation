"""Product listing and sorting."""
import pytest
from playwright.sync_api import expect

from conftest import PASSWORD, PROBLEM_USER
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_inventory_shows_six_products(logged_in):
    expect(logged_in.title).to_have_text("Products")
    expect(logged_in.items).to_have_count(6)


@pytest.mark.parametrize(
    "option, key, reverse",
    [
        ("az", "names", False),
        ("za", "names", True),
        ("lohi", "prices", False),
        ("hilo", "prices", True),
    ],
    ids=["name-a-z", "name-z-a", "price-low-high", "price-high-low"],
)
def test_sorting(logged_in, option, key, reverse):
    logged_in.sort_by(option)
    values = getattr(logged_in, key)()
    assert values == sorted(values, reverse=reverse)


@pytest.mark.xfail(reason="BUG-001: problem_user sees the same image for every product", strict=True)
def test_problem_user_product_images_are_unique(login_page, page):
    login_page.login(PROBLEM_USER, PASSWORD)
    inventory = InventoryPage(page)
    expect(inventory.item_images).to_have_count(6)  # wait for images to render
    sources = [img.get_attribute("src") for img in inventory.item_images.all()]
    assert len(set(sources)) == len(sources)
