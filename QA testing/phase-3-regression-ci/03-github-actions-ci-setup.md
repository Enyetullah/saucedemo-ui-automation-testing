# GitHub Actions CI Setup - Phase 3

## Purpose

This file documents the GitHub Actions setup used to run the Playwright + Pytest regression suite automatically.

## Workflow Location

The workflow file should be placed at:

```text
.github/workflows/playwright-regression.yml
```

## Workflow Triggers

The workflow runs on:

- Push to `main` or `master`
- Pull request to `main` or `master`
- Manual run from the GitHub Actions tab

## Workflow Steps

| Step | Purpose |
|---|---|
| Checkout repository | Pulls the project code into the GitHub runner |
| Set up Python | Installs the selected Python version |
| Install dependencies | Installs packages from `requirements.txt` |
| Install Playwright Chromium | Installs the browser needed for UI tests |
| Run regression tests | Executes `pytest -v` |

## Workflow File

```yaml
name: SauceDemo Regression UI Tests

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  regression-tests:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Install Playwright Chromium
        run: python -m playwright install --with-deps chromium

      - name: Run Playwright regression tests
        run: pytest -v
```

## How to Verify CI

1. Commit the workflow file.
2. Push the project to GitHub.
3. Open the repository on GitHub.
4. Click the Actions tab.
5. Open the latest workflow run.
6. Confirm that the regression tests passed.

## Expected CI Result

```text
31 passed
```
