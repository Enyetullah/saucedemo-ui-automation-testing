from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.cancel_button = page.locator("#cancel")
        self.error_message = page.locator('[data-test="error"]')
        self.complete_header = page.locator(".complete-header")

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish(self):
        self.finish_button.click()

    def cancel(self):
        self.cancel_button.click()

    def expect_error_contains(self, expected_text: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(expected_text)
