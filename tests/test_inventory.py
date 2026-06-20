from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


def test_products_page_loads_after_login(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.expect_loaded()
    expect(inventory.product_names.first).to_be_visible()
    expect(inventory.product_prices.first).to_be_visible()


def test_open_product_details_and_return_to_products(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    first_product_name = inventory.product_names.first.inner_text()
    inventory.open_first_product_details()

    expect(logged_in_page.locator(".inventory_details_name")).to_have_text(first_product_name)
    logged_in_page.locator("#back-to-products").click()
    inventory.expect_loaded()


def test_sort_products_name_a_to_z(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.select_sort_option("az")
    names = inventory.get_product_names()

    assert names == sorted(names)


def test_sort_products_name_z_to_a(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.select_sort_option("za")
    names = inventory.get_product_names()

    assert names == sorted(names, reverse=True)


def test_sort_products_price_low_to_high(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.select_sort_option("lohi")
    prices = inventory.get_product_prices()

    assert prices == sorted(prices)


def test_sort_products_price_high_to_low(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.select_sort_option("hilo")
    prices = inventory.get_product_prices()

    assert prices == sorted(prices, reverse=True)
