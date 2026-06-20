import re
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from tests.conftest import STANDARD_USER, LOCKED_OUT_USER, PASSWORD


def test_valid_login_with_standard_user(login_page, page):
    login_page.login(STANDARD_USER, PASSWORD)

    inventory = InventoryPage(page)
    inventory.expect_loaded()
    expect(page).to_have_url(re.compile(".*inventory\\.html.*"))


def test_locked_out_user_shows_error(login_page):
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    login_page.expect_error_contains("locked out")


def test_invalid_username_and_password_show_error(login_page):
    login_page.login("invalid_user", "wrong_password")

    login_page.expect_error_contains("Username and password do not match")


def test_empty_login_form_shows_username_required(login_page):
    login_page.login_button.click()

    login_page.expect_error_contains("Username is required")


def test_username_without_password_shows_password_required(login_page):
    login_page.username_input.fill(STANDARD_USER)
    login_page.login_button.click()

    login_page.expect_error_contains("Password is required")


def test_password_without_username_shows_username_required(login_page):
    login_page.password_input.fill(PASSWORD)
    login_page.login_button.click()

    login_page.expect_error_contains("Username is required")