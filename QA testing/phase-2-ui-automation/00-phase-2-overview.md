# Phase 2 Overview - UI Automation

## Project

SauceDemo UI Automation Testing Project

## Phase

Phase 2: UI Automation with Playwright and Pytest

## Objective

The objective of this phase is to automate the main SauceDemo browser workflows that were manually tested in Phase 1.

The automated suite covers:

- Login behavior
- Login validation errors
- Locked-out user behavior
- Inventory page loading
- Product details navigation
- Product sorting
- Cart add/remove behavior
- Checkout validation
- Successful checkout
- Logout behavior
- Direct protected page access without login

## Scope

This phase focuses on browser-based UI automation. API and database testing are not included because SauceDemo is being used as an external application under test.

## Tooling

| Tool | Purpose |
|---|---|
| Python | Test programming language |
| Pytest | Test runner |
| Playwright | Browser automation |
| Chromium | Browser used for automated execution |

## Execution Command

```bash
pytest -v
```

## Notes

The tests use Page Object Model structure to keep page locators and test logic separate.
