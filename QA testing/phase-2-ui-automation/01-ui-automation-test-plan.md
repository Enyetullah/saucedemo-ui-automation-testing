# UI Automation Test Plan - Phase 2

## Application Under Test

SauceDemo / Swag Labs

## Test Type

Automated UI testing

## Objective

Validate key ecommerce workflows through automated browser tests.

## In Scope

| Area | Included Tests |
|---|---|
| Login | Valid login, invalid login, empty fields, locked-out user |
| Inventory | Product list, product details, return navigation |
| Sorting | Name and price sorting |
| Cart | Add item, remove item, cart badge, cart page |
| Checkout | Required fields, valid checkout, order completion, cancel checkout |
| Session | Logout, protected page access without login |

## Out of Scope

- Backend API testing
- Database validation
- Payment processing
- Real order fulfillment
- Cross-browser testing beyond Chromium for this phase

## Test Environment

| Field | Value |
|---|---|
| Application URL | `https://www.saucedemo.com/` |
| Browser | Chromium |
| Language | Python |
| Framework | Pytest |
| Automation Tool | Playwright |

## Entry Criteria

- Test environment is installed.
- Browser binaries are installed with Playwright.
- SauceDemo is accessible.
- Test files are available in the `tests/` folder.

## Exit Criteria

- Automated tests execute through `pytest -v`.
- Results are documented.
- Any failed tests are reviewed and documented.
