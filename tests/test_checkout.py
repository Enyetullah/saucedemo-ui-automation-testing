from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def start_checkout_with_one_item(page):
    inventory = InventoryPage(page)
    inventory.add_product_by_index(0)
    inventory.open_cart()
    cart = CartPage(page)
    cart.checkout()
    checkout = CheckoutPage(page)
    expect(checkout.title).to_have_text("Checkout: Your Information")
    return checkout


def test_start_checkout_opens_information_page(logged_in_page):
    checkout = start_checkout_with_one_item(logged_in_page)

    expect(checkout.first_name_input).to_be_visible()
    expect(checkout.last_name_input).to_be_visible()
    expect(checkout.postal_code_input).to_be_visible()


def test_checkout_with_valid_information_opens_overview(logged_in_page):
    checkout = start_checkout_with_one_item(logged_in_page)

    checkout.fill_information("John", "Doe", "12345")
    checkout.continue_checkout()

    expect(logged_in_page.locator(".title")).to_have_text("Checkout: Overview")


def test_complete_order_displays_success_message(logged_in_page):
    checkout = start_checkout_with_one_item(logged_in_page)

    checkout.fill_information("John", "Doe", "12345")
    checkout.continue_checkout()
    checkout.finish()

    expect(logged_in_page.locator(".title")).to_have_text("Checkout: Complete!")
    expect(checkout.complete_header).to_have_text("Thank you for your order!")


def test_cancel_checkout_returns_to_cart(logged_in_page):
    checkout = start_checkout_with_one_item(logged_in_page)

    checkout.cancel()

    expect(logged_in_page.locator(".title")).to_have_text("Your Cart")


def test_checkout_missing_first_name_shows_error(logged_in_page):
    checkout = start_checkout_with_one_item(logged_in_page)

    checkout.fill_information("", "Doe", "12345")
    checkout.continue_checkout()

    checkout.expect_error_contains("First Name is required")


def test_checkout_missing_last_name_shows_error(logged_in_page):
    checkout = start_checkout_with_one_item(logged_in_page)

    checkout.fill_information("John", "", "12345")
    checkout.continue_checkout()

    checkout.expect_error_contains("Last Name is required")


def test_checkout_missing_postal_code_shows_error(logged_in_page):
    checkout = start_checkout_with_one_item(logged_in_page)

    checkout.fill_information("John", "Doe", "")
    checkout.continue_checkout()

    checkout.expect_error_contains("Postal Code is required")


def test_checkout_accepts_special_characters_without_breaking(logged_in_page):
    checkout = start_checkout_with_one_item(logged_in_page)

    checkout.fill_information("@John!", "#Doe$", "12345")
    checkout.continue_checkout()

    expect(logged_in_page.locator(".title")).to_have_text("Checkout: Overview")
