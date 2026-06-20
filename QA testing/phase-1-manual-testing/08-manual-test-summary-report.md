# Manual Test Summary Report - Phase 1

## Project Name

SauceDemo UI Automation Testing Project

## Application Under Test

SauceDemo / Swag Labs

## Testing Phase

Phase 1: Manual UI Testing

## Objective

Manual UI testing was performed to validate the main ecommerce workflows in SauceDemo, including login, product browsing, sorting, cart management, checkout, logout, session behavior, and negative/edge scenarios.

## Test Coverage

| Area | Coverage |
|---|---|
| Login | Valid login, invalid login, locked-out user, empty fields |
| Inventory | Product list, product details, navigation |
| Sorting | Name and price sorting |
| Cart | Add item, remove item, cart badge, cart page |
| Checkout | Required fields, valid checkout, overview, completion |
| Logout | Menu access and logout behavior |
| Session | Protected page access after logout |
| User Types | Problem user and performance glitch user behavior |

## Execution Status

| Status | Count |
|---|---:|
| Passed | 27 |
| Failed | 0 |
| Blocked | 0 |
| Needs Improvement | 0 |
| Not Run | 0 |
| Total | 27 |

## Negative and Edge Test Status

| Status | Count |
|---|---:|
| Passed | 16 |
| Failed | 0 |
| Blocked | 0 |
| Needs Improvement | 0 |
| Not Run | 0 |
| Total | 16 |

## Overall Phase 1 Status

| Status | Count |
|---|---:|
| Passed | 43 |
| Failed | 0 |
| Blocked | 0 |
| Needs Improvement | 0 |
| Not Run | 0 |
| Total | 43 |

## Screenshot Evidence Captured

| Screenshot File | Related Test |
|---|---|
| `screenshots/tc-001-valid-login.png` | TC-001, TC-007 |
| `screenshots/tc-015-add-to-cart.png` | TC-015 |
| `screenshots/tc-018-cart-page.png` | TC-018 |
| `screenshots/tc-022-checkout-overview.png` | TC-022 |
| `screenshots/tc-023-order-complete.png` | TC-023 |
| `screenshots/net-005-locked-out-user.png` | NET-005 |

## Findings

| Finding | Status |
|---|---|
| Valid login with `standard_user` worked successfully. | Passed |
| Locked-out user login was blocked with an error message. | Passed |
| Invalid login and empty-field validation worked as expected. | Passed |
| Product list, product details, and product navigation worked correctly. | Passed |
| Product sorting worked for name and price sorting options. | Passed |
| Cart add, remove, badge count, and cart page behavior worked correctly. | Passed |
| Checkout required-field validation worked correctly. | Passed |
| Valid checkout flow completed successfully. | Passed |
| Logout returned the user to the login page. | Passed |
| Direct access to protected pages after logout was blocked or redirected appropriately. | Passed |
| Problem user behavior was reviewed and documented as an observation. | Documented |
| Performance glitch user delay was reviewed and documented as an observation. | Documented |

## Bugs Found

No confirmed bugs were found during Phase 1 manual UI testing.

| Bug ID | Summary | Severity | Status |
|---|---|---|---|
| N/A | No confirmed bugs found during this phase. | N/A | N/A |

## Notes

- All planned manual test cases were executed.
- All planned negative and edge test cases were executed.
- All test cases passed during execution.
- Screenshot evidence was captured for important workflows.
- No confirmed defects were identified during this phase.
- The `problem_user` and `performance_glitch_user` accounts were treated as special test users and documented as observations rather than defects.
- This phase is complete and ready to support the next phase of testing.

## Conclusion

Phase 1 manual UI testing was completed successfully.

A total of 43 test cases were executed, including 27 manual workflow test cases and 16 negative/edge test cases. All 43 tests passed, with no failed, blocked, or not-run test cases.

The main SauceDemo workflows behaved as expected, including login, inventory browsing, sorting, cart management, checkout, logout, and protected page access after logout.

No confirmed bugs were found during this phase. The project is ready to move into Phase 2 UI automation testing.