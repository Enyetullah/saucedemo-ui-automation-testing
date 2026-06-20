# UI Automation Execution Report - Phase 2

## Test Session Information

| Field | Value |
|---|---|
| Tester | Enyetullah Rahimullah |
| Date | 2026-06-19 |
| Tool | Playwright + Pytest |
| Browser | Chromium |
| Test Command | `pytest -v` |
| Application URL | `https://www.saucedemo.com/` |
| Browser Required? | Automated browser launched by Playwright |

## Execution Summary

| Status | Count |
|---|---:|
| Passed | 31 |
| Failed | 0 |
| Skipped | 0 |
| Errors | 0 |
| Total | 31 |

## Execution Notes

- Automated UI tests were executed using Playwright with Chromium.
- Tests were organized using the Page Object Model.
- The test suite validated login, invalid login, locked-out user behavior, inventory page loading, product sorting, cart actions, checkout flow, logout, and protected page access.
- One test code issue was found during execution and fixed by updating the URL assertion to use a regular expression instead of a lambda function.
- After the fix, all automated UI tests passed successfully.

## Result Details

```text
31 passed
```

## Tested Areas

| Area | Result |
|---|---|
| Valid login | Passed |
| Locked-out user login | Passed |
| Invalid login | Passed |
| Empty username/password validation | Passed |
| Inventory page loading | Passed |
| Product details navigation | Passed |
| Product sorting by name | Passed |
| Product sorting by price | Passed |
| Add item to cart | Passed |
| Add multiple items to cart | Passed |
| Remove item from products page | Passed |
| Cart page item display | Passed |
| Remove item from cart page | Passed |
| Continue shopping from cart | Passed |
| Checkout information page | Passed |
| Checkout overview page | Passed |
| Complete checkout flow | Passed |
| Cancel checkout | Passed |
| Checkout required-field validation | Passed |
| Special character checkout input | Passed |
| Menu and logout behavior | Passed |
| Direct protected-page access without login | Passed |
| Access inventory after logout | Passed |

## Conclusion

Phase 2 UI automation testing was completed successfully.

The automated Playwright + Pytest suite executed 31 tests against SauceDemo / Swag Labs. All 31 tests passed, with no failed, skipped, or error results.

This phase confirms that the main UI workflows are covered by automated browser tests, including login, inventory, sorting, cart, checkout, logout, validation, and protected page access.