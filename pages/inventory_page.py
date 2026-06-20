from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def expect_loaded(self):
        expect(self.title).to_have_text("Products")
        expect(self.inventory_items).to_have_count(6)

    def add_product_by_index(self, index: int = 0):
        self.inventory_items.nth(index).locator("button").click()

    def remove_product_by_index(self, index: int = 0):
        self.inventory_items.nth(index).locator("button").click()

    def open_cart(self):
        self.cart_link.click()

    def open_first_product_details(self):
        self.product_names.first.click()

    def select_sort_option(self, option_value: str):
        self.sort_dropdown.select_option(option_value)

    def get_product_names(self):
        return self.product_names.all_inner_texts()

    def get_product_prices(self):
        prices = []
        for price_text in self.product_prices.all_inner_texts():
            prices.append(float(price_text.replace("$", "")))
        return prices

    def logout(self):
        self.menu_button.click()
        expect(self.logout_link).to_be_visible()
        self.logout_link.click()
