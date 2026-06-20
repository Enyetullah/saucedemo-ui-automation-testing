# Regression Test Suite - Phase 3

## Regression Suite Summary

The regression suite contains the automated UI tests from Phase 2. These tests validate the core SauceDemo user workflows.

## Test Groups

| Test Group | Purpose | Status |
|---|---|---|
| Login tests | Validate successful login, invalid login, locked-out user, and required-field errors | Automated |
| Inventory tests | Validate inventory page loading and product details navigation | Automated |
| Sorting tests | Validate product sorting by name and price | Automated |
| Cart tests | Validate add/remove item behavior and cart badge updates | Automated |
| Checkout tests | Validate required fields, checkout overview, order completion, and cancel behavior | Automated |
| Session/navigation tests | Validate logout and protected page behavior | Automated |

## Regression Command

Run the full regression suite locally with:

```bash
pytest -v
```

Run with visible browser mode when debugging:

```bash
pytest -v --headed
```

## Expected Result

The expected local regression result is:

```text
31 passed
```

## Regression Suite Notes

- Tests are written with Playwright and Pytest.
- Page Object Model is used to keep page actions organized.
- The suite focuses on stable functional workflows.
- No confirmed application defects were found during Phase 2 automation execution.
