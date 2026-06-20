from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def expect_loaded(self):
        expect(self.title).to_have_text("Your Cart")

    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def remove_first_item(self):
        self.cart_items.first.locator("button").click()
