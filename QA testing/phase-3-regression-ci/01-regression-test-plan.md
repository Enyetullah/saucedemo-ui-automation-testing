# Regression Test Plan - Phase 3

## Objective

The objective of this regression test plan is to verify that the main SauceDemo workflows continue to function correctly through repeatable automated UI tests.

## Regression Strategy

The regression suite reuses the Playwright + Pytest tests created in Phase 2. These tests are treated as the baseline regression set for future executions.

Regression testing is performed in two ways:

1. Local execution using `pytest -v`
2. CI execution using GitHub Actions

## Test Environment

| Field | Value |
|---|---|
| Application URL | `https://www.saucedemo.com/` |
| Browser | Chromium |
| Automation Tool | Playwright |
| Test Runner | Pytest |
| CI Tool | GitHub Actions |

## Entry Criteria

- Phase 1 manual testing is complete.
- Phase 2 UI automation tests are created.
- Python dependencies are installed.
- Playwright Chromium browser is installed.
- Test suite passes locally before being added to CI.

## Exit Criteria

- Regression suite runs successfully.
- Test results are documented.
- GitHub Actions workflow is added.
- CI execution result is reviewed after push.

## Risks

| Risk | Mitigation |
|---|---|
| SauceDemo site may be temporarily unavailable | Re-run tests after confirming site availability |
| UI changes may break selectors | Update Page Object Model locators |
| Network delays may affect tests | Use Playwright auto-waiting and stable assertions |
| CI browser dependency issues | Install Playwright Chromium in the workflow |
