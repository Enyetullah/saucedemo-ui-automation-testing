# Playwright Setup Guide - Phase 2

## 1. Create and Activate Virtual Environment

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 2. Install Requirements

```bash
pip install -r requirements.txt
```

## 3. Install Playwright Browser

```bash
python -m playwright install chromium
```

## 4. Run Tests

```bash
pytest -v
```

## 5. Run Tests with Browser Visible

On macOS/Linux:

```bash
HEADED=true pytest -v
```

On Windows PowerShell:

```powershell
$env:HEADED="true"
pytest -v
```

## 6. Optional Slow Motion Mode

On Windows PowerShell:

```powershell
$env:HEADED="true"
$env:SLOW_MO="300"
pytest -v
```

## Troubleshooting

If Playwright cannot find a browser, run:

```bash
python -m playwright install chromium
```

If pytest cannot find the page object files, make sure the project folder contains both:

```text
pages/
tests/
```
