# Phase 1 Overview - Manual UI Testing

## Project Name

SauceDemo UI Automation Testing Project

## Application Under Test

SauceDemo / Swag Labs

## Application URL

`https://www.saucedemo.com/`

## Phase

Phase 1: Manual UI Testing

## Purpose

This phase documents manual UI testing for the SauceDemo ecommerce demo application. The goal is to validate the main user workflows.

## Features Covered

- Login with valid user
- Login with locked-out user
- Login with invalid credentials
- Product inventory page
- Product sorting
- Add item to cart
- Remove item from cart
- Cart page navigation
- Checkout information validation
- Checkout overview
- Order completion
- Logout

## Test Accounts

| User Type | Username | Password |
|---|---|---|
| Standard user | `standard_user` | `secret_sauce` |
| Locked-out user | `locked_out_user` | `secret_sauce` |
| Problem user | `problem_user` | `secret_sauce` |
| Performance glitch user | `performance_glitch_user` | `secret_sauce` |

## Testing Scope

### In Scope

- Functional UI testing
- Positive test cases
- Negative test cases
- Edge cases
- Basic regression checks
- Screenshot evidence
- Bug reports and findings

### Out of Scope

- Backend/database validation
- API testing
- Performance testing beyond visible page delay observations
- Security penetration testing
- Source-code review

## Notes

This repository is for QA testing documentation and automation. It does not claim ownership of the SauceDemo application source code.
