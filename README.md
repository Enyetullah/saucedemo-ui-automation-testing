# SauceDemo UI Automation Testing Project

This project contains QA documentation and automated UI tests for SauceDemo / Swag Labs.

## Phase 2: UI Automation

Automated browser tests were created with Playwright and Pytest. The tests cover login, inventory, sorting, cart, checkout, logout, and protected-route behavior.

## How to Run

```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

To run with the browser visible:

```bash
HEADED=true pytest -v
```

On Windows PowerShell:

```powershell
$env:HEADED="true"
pytest -v
```
