# UI Automation Summary Report - Phase 2

## Project Name

SauceDemo UI Automation Testing Project

## Application Under Test

SauceDemo / Swag Labs

## Testing Phase

Phase 2: UI Automation with Playwright and Pytest

## Objective

Automated UI testing was performed to validate the main SauceDemo ecommerce workflows through repeatable browser-based tests.

The automated test suite focused on login, product browsing, sorting, cart behavior, checkout validation, order completion, logout, and protected page access.

## Automated Areas Covered

| Area | Coverage |
|---|---|
| Login | Valid login, invalid login, locked-out user, empty fields |
| Inventory | Product page load and product details navigation |
| Sorting | Name and price sorting |
| Cart | Add item, remove item, badge updates, cart page |
| Checkout | Required fields, valid checkout, completion, cancel checkout |
| Session | Logout and direct protected page access without login |

## Execution Status

| Status | Count |
|---|---:|
| Passed | 31 |
| Failed | 0 |
| Skipped | 0 |
| Errors | 0 |
| Not Run | 0 |
| Total | 31 |

## Tools Used

| Tool | Purpose |
|---|---|
| Playwright | Browser automation |
| Pytest | Test execution framework |
| Chromium | Automated browser |
| Page Object Model | Test organization and reusable page actions |

## Test Results Summary

| Area | Result |
|---|---|
| Valid login with standard user | Passed |
| Locked-out user validation | Passed |
| Invalid login validation | Passed |
| Empty field login validation | Passed |
| Inventory page loading | Passed |
| Product details navigation | Passed |
| Product sorting | Passed |
| Add/remove cart actions | Passed |
| Cart page validation | Passed |
| Checkout field validation | Passed |
| Checkout completion flow | Passed |
| Checkout cancellation | Passed |
| Logout behavior | Passed |
| Protected page access without login | Passed |

## Notes

- Tests were executed with the command `pytest -v`.
- Playwright launched Chromium automatically during test execution.
- Tests were organized using the Page Object Model.
- The full automated UI test suite passed successfully.
- One test code issue was found during execution and fixed by replacing an invalid URL assertion with a regular expression-based assertion.
- No application bugs were confirmed during this automation phase.

## Bugs Found

No confirmed application bugs were found during Phase 2 UI automation testing.

| Bug ID | Summary | Severity | Status |
|---|---|---|---|
| N/A | No confirmed bugs found during this phase. | N/A | N/A |

## Conclusion

Phase 2 UI automation testing was completed successfully.

A total of 31 automated UI tests were executed using Playwright and Pytest. All 31 tests passed, with no failed, skipped, or error results.

The automated suite confirms that the main SauceDemo workflows are covered by repeatable browser-based tests, including login, inventory browsing, sorting, cart management, checkout, logout, validation behavior, and protected page access.

This phase is complete and ready to support future regression testing.