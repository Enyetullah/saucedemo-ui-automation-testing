from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_one_product_to_cart_updates_badge(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.add_product_by_index(0)

    expect(inventory.cart_badge).to_have_text("1")
    expect(inventory.inventory_items.nth(0).locator("button")).to_have_text("Remove")


def test_add_multiple_products_to_cart_updates_badge(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.add_product_by_index(0)
    inventory.add_product_by_index(1)

    expect(inventory.cart_badge).to_have_text("2")


def test_remove_product_from_products_page_updates_badge(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.add_product_by_index(0)
    expect(inventory.cart_badge).to_have_text("1")
    inventory.remove_product_by_index(0)

    expect(inventory.inventory_items.nth(0).locator("button")).to_have_text("Add to cart")
    expect(inventory.cart_badge).to_have_count(0)


def test_cart_page_displays_selected_product(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    selected_product = inventory.product_names.first.inner_text()

    inventory.add_product_by_index(0)
    inventory.open_cart()

    cart = CartPage(logged_in_page)
    cart.expect_loaded()
    expect(cart.cart_items).to_have_count(1)
    expect(logged_in_page.locator(".inventory_item_name")).to_have_text(selected_product)


def test_remove_item_from_cart_page(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_product_by_index(0)
    inventory.open_cart()

    cart = CartPage(logged_in_page)
    cart.remove_first_item()

    expect(cart.cart_items).to_have_count(0)
    expect(cart.cart_badge).to_have_count(0)


def test_continue_shopping_returns_to_products_page(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.open_cart()

    cart = CartPage(logged_in_page)
    cart.continue_shopping()

    inventory.expect_loaded()
