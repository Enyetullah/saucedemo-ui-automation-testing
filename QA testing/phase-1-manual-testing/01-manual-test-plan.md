# Manual Test Plan - Phase 1

## Project Name

SauceDemo UI Automation Testing Project

## Application Under Test

SauceDemo / Swag Labs

## URL

`https://www.saucedemo.com/`

## Objective

The objective of this test plan is to manually validate the main SauceDemo user workflows, including login, inventory browsing, cart management, checkout, and logout.

## Testing Approach

Testing will be performed manually through a web browser. Each test case will include clear steps, expected results, actual results, status, and screenshot evidence when needed.

## Browser Environment

| Item | Value |
|---|---|
| Browser | Chrome / Edge |
| Operating System | Windows |
| Internet Required | Yes |
| Test Type | Manual UI Testing |

## Test Data

| Field | Value |
|---|---|
| Standard Username | `standard_user` |
| Locked Username | `locked_out_user` |
| Password | `secret_sauce` |
| Invalid Username | `invalid_user` |
| Invalid Password | `wrong_password` |
| Checkout First Name | `John` |
| Checkout Last Name | `Doe` |
| Checkout Postal Code | `12345` |

## Features to Test

| Feature | Description |
|---|---|
| Login | Validate successful and unsuccessful login behavior |
| Inventory | Validate product list display |
| Sorting | Validate product sorting dropdown behavior |
| Cart | Validate add/remove item workflows |
| Checkout | Validate checkout form, overview, and completion |
| Logout | Validate user can log out and return to login page |

## Entry Criteria

- SauceDemo website is accessible.
- Browser is working.
- Test credentials are available.
- Test cases are prepared.

## Exit Criteria

- Manual test cases are executed.
- Passed, failed, blocked, and not run results are recorded.
- Bug reports are documented for failed cases.
- Screenshots are saved for important evidence.
- Summary report is completed.

## Status Definitions

| Status | Meaning |
|---|---|
| Pass | Actual result matched expected result |
| Fail | Actual result did not match expected result |
| Blocked | Test could not be completed due to external issue |
| Not Run | Test was not executed yet |
| Needs Improvement | Feature works but behavior could be improved |
