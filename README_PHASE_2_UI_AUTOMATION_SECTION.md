## QA Testing - Phase 2: UI Automation with Playwright and Pytest

UI automation was added for SauceDemo / Swag Labs using Playwright and Pytest. The automated test suite validates the main browser workflows that were covered during manual testing, including login, product browsing, sorting, cart management, checkout validation, logout, and protected page access.

Phase 2 documentation is available in:

`qa-documentation/phase-2-ui-automation/`

Automation files are available in:

`tests/`

Page object files are available in:

`pages/`

To run the tests:

```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

The automated suite includes positive workflow tests, negative validation tests, and session/navigation protection checks.
