# SauceDemo UI Automation Testing Project

## Project Overview

This project contains QA documentation, Playwright UI automation, regression testing, and GitHub Actions CI setup for the SauceDemo / Swag Labs demo e-commerce application.

The goal of this project is to validate the main user workflows of an online shopping application through structured manual test documentation and repeatable automated UI tests.

## Application Under Test

| Item | Details |
|---|---|
| Application | SauceDemo / Swag Labs |
| URL | https://www.saucedemo.com/ |
| Application Type | Demo e-commerce web application |
| Main Test User | `standard_user` |
| Locked User | `locked_out_user` |
| Password | `secret_sauce` |

## Project Highlights

- Created manual QA documentation for major e-commerce workflows
- Built automated UI tests using Playwright and Pytest
- Used the Page Object Model for cleaner test structure
- Covered positive, negative, and session-protection scenarios
- Organized the automated suite as a regression test suite
- Added GitHub Actions CI workflow for automated test execution

## Tech Stack

| Category | Tools |
|---|---|
| Programming Language | Python |
| Test Framework | Pytest |
| Browser Automation | Playwright |
| Design Pattern | Page Object Model |
| CI/CD | GitHub Actions |
| Version Control | Git and GitHub |
| Application Tested | SauceDemo / Swag Labs |

## Test Coverage

The automated regression suite covers the following areas:

| Area | Coverage |
|---|---|
| Login | Valid login, invalid login, locked-out user, empty username, empty password |
| Inventory | Product page loading, product details navigation |
| Sorting | Sort by name A-Z, name Z-A, price low-high, price high-low |
| Cart | Add item, remove item, cart badge updates, cart page validation |
| Checkout | Checkout information form, required field validation, order overview, order completion |
| Session and Navigation | Logout, protected page access without login, access after logout |
| Regression | Full automated UI regression suite |
| CI Automation | GitHub Actions workflow for automated regression execution |

## Test Execution Summary

| Phase | Area | Status |
|---|---|---|
| Phase 1 | Manual UI Testing Documentation | Prepared |
| Phase 2 | Playwright UI Automation | Completed |
| Phase 3 | Regression Testing and CI Automation | Completed |

## Automated Regression Result

```text
31 automated UI tests passed
0 failed
0 skipped
0 errors
```

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── playwright-regression.yml
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_session_and_navigation.py
│
├── qa-documentation/
│   ├── phase-1-manual-testing/
│   ├── phase-2-ui-automation/
│   └── phase-3-regression-ci/
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Page Object Model

The automation code uses the Page Object Model to keep page actions separate from test cases.

| Page Object | Purpose |
|---|---|
| `login_page.py` | Login page actions and login validation |
| `inventory_page.py` | Product list, sorting, cart badge, and logout actions |
| `cart_page.py` | Cart page validation and cart actions |
| `checkout_page.py` | Checkout form, overview, and order completion actions |

## Automated Test Files

| Test File | Coverage |
|---|---|
| `test_login.py` | Valid login, invalid login, locked-out user, empty field validation |
| `test_inventory.py` | Product page loading, product details, and sorting |
| `test_cart.py` | Add to cart, remove from cart, cart badge, and cart navigation |
| `test_checkout.py` | Checkout form validation, checkout overview, order completion, and cancel flow |
| `test_session_and_navigation.py` | Logout and protected-route behavior |

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Create a Virtual Environment

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browser

```bash
python -m playwright install chromium
```

## Running the Tests

### Run All Tests

```bash
pytest -v
```

### Run Tests with Browser Visible

#### Windows PowerShell

```powershell
$env:HEADED="true"
pytest -v
```

#### macOS / Linux

```bash
HEADED=true pytest -v
```

### Run with Slow Motion

#### Windows PowerShell

```powershell
$env:HEADED="true"
$env:SLOW_MO="300"
pytest -v
```

#### macOS / Linux

```bash
HEADED=true SLOW_MO=300 pytest -v
```

## GitHub Actions CI

This project includes a GitHub Actions workflow that runs the Playwright regression suite automatically.

Workflow file:

```text
.github/workflows/playwright-regression.yml
```

The workflow runs on:

- Push events
- Pull request events
- Manual workflow dispatch

The CI workflow installs dependencies, installs Playwright Chromium, and runs:

```bash
pytest -v
```

## QA Documentation

The `qa-documentation/` folder contains structured QA documentation for each project phase.

| Folder | Purpose |
|---|---|
| `phase-1-manual-testing/` | Manual test plan, scenarios, test cases, negative tests, bug report template, and summary report |
| `phase-2-ui-automation/` | UI automation test plan, setup guide, automated test cases, execution report template, and summary report |
| `phase-3-regression-ci/` | Regression test plan, regression suite, CI setup, local execution report, and CI report template |

## Key Workflows Tested

### Login Workflow

- Standard user login
- Locked-out user validation
- Invalid credentials validation
- Empty username validation
- Empty password validation

### Inventory Workflow

- Product page loading
- Product details navigation
- Sorting by product name
- Sorting by product price

### Cart Workflow

- Add one product to cart
- Add multiple products to cart
- Remove product from product page
- Remove product from cart page
- Continue shopping from cart

### Checkout Workflow

- Start checkout
- Required field validation
- Valid checkout information
- Checkout overview
- Complete order
- Cancel checkout

### Session Workflow

- Logout
- Block direct inventory access without login
- Block direct cart access without login
- Block direct checkout access without login
- Block inventory access after logout

## Final Project Result

```text
Automated UI Tests: 31 passed
Failures: 0
Skipped: 0
Errors: 0
Confirmed Bugs: 0
```

## Notes

This project uses SauceDemo as a public demo application for QA practice. The focus of this repository is test design, automation structure, regression testing, and CI readiness.

## Author

Enyetullah Rahimullah
