import os
import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

STANDARD_USER = "standard_user"
LOCKED_OUT_USER = "locked_out_user"
PROBLEM_USER = "problem_user"
PERFORMANCE_GLITCH_USER = "performance_glitch_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("SAUCEDEMO_BASE_URL", "https://www.saucedemo.com/")


@pytest.fixture(scope="session")
def browser():
    headed = os.getenv("HEADED", "false").lower() in {"1", "true", "yes"}
    slow_mo = int(os.getenv("SLOW_MO", "0"))

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=not headed, slow_mo=slow_mo)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture()
def login_page(page, base_url):
    login = LoginPage(page, base_url)
    login.goto()
    return login


@pytest.fixture()
def logged_in_page(page, base_url):
    login = LoginPage(page, base_url)
    login.goto()
    login.login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(page)
    inventory.expect_loaded()
    return page
