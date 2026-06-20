from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from tests.conftest import STANDARD_USER, PASSWORD


def test_menu_opens_and_logout_returns_to_login(logged_in_page, base_url):
    inventory = InventoryPage(logged_in_page)

    inventory.logout()

    login = LoginPage(logged_in_page, base_url)
    login.expect_login_page()


def test_direct_access_to_inventory_without_login_is_blocked(page, base_url):
    page.goto(base_url.rstrip("/") + "/inventory.html")

    login = LoginPage(page, base_url)
    login.expect_login_page()
    login.expect_error_contains("You can only access")


def test_direct_access_to_cart_without_login_is_blocked(page, base_url):
    page.goto(base_url.rstrip("/") + "/cart.html")

    login = LoginPage(page, base_url)
    login.expect_login_page()
    login.expect_error_contains("You can only access")


def test_direct_access_to_checkout_without_login_is_blocked(page, base_url):
    page.goto(base_url.rstrip("/") + "/checkout-step-one.html")

    login = LoginPage(page, base_url)
    login.expect_login_page()
    login.expect_error_contains("You can only access")


def test_access_inventory_after_logout_is_blocked(page, base_url):
    login = LoginPage(page, base_url)
    login.goto()
    login.login(STANDARD_USER, PASSWORD)

    inventory = InventoryPage(page)
    inventory.expect_loaded()
    inventory.logout()

    page.goto(base_url.rstrip("/") + "/inventory.html")
    login.expect_login_page()
    login.expect_error_contains("You can only access")
