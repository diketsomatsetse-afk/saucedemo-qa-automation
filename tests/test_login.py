"""Login: valid, invalid and blocked accounts."""
import re

import pytest
from playwright.sync_api import expect

from conftest import LOCKED_OUT_USER, PASSWORD, STANDARD_USER


@pytest.mark.smoke
def test_valid_login_opens_inventory(login_page, page):
    login_page.login(STANDARD_USER, PASSWORD)
    expect(page).to_have_url(re.compile(r"/inventory\.html$"))


def test_locked_out_user_sees_error(login_page):
    login_page.login(LOCKED_OUT_USER, PASSWORD)
    expect(login_page.error).to_contain_text("this user has been locked out")


def test_wrong_password_is_rejected(login_page):
    login_page.login(STANDARD_USER, "wrong_password")
    expect(login_page.error).to_contain_text("Username and password do not match")


@pytest.mark.parametrize(
    "username, password, message",
    [
        ("", PASSWORD, "Username is required"),
        (STANDARD_USER, "", "Password is required"),
    ],
    ids=["missing-username", "missing-password"],
)
def test_required_fields(login_page, username, password, message):
    login_page.login(username, password)
    expect(login_page.error).to_contain_text(message)


def test_inventory_requires_login(page):
    """Opening a protected page directly must bounce back to login."""
    page.goto("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "You can only access '/inventory.html' when you are logged in"
    )
