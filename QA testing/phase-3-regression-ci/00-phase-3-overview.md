# Phase 3 Overview: Regression Testing and CI Automation

## Project Name

SauceDemo UI Automation Testing Project

## Application Under Test

SauceDemo / Swag Labs

## Phase

Phase 3: Regression Testing and CI Automation

## Purpose

Phase 3 uses the automated Playwright + Pytest test suite as a repeatable regression suite. The goal is to confirm that the main SauceDemo workflows continue to work after changes to the test code, documentation, or project setup.

This phase also adds GitHub Actions so the regression suite can run automatically when code is pushed to GitHub or when a pull request is opened.

## Scope

The regression suite covers:

- Login behavior
- Locked-out user behavior
- Invalid and empty login validation
- Inventory page loading
- Product details navigation
- Product sorting
- Cart add/remove behavior
- Checkout validation
- Checkout completion
- Logout
- Protected page access without login

## Out of Scope

- Backend API testing
- Database validation
- Performance/load testing
- Visual snapshot testing
- Mobile browser testing

## Tools Used

| Tool | Purpose |
|---|---|
| Playwright | Browser automation |
| Pytest | Test execution framework |
| Chromium | Automated browser |
| GitHub Actions | CI automation |
| Page Object Model | Test organization and reusable page actions |
