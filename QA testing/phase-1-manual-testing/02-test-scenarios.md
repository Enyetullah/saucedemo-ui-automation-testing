# Test Scenarios - Phase 1

## Login Scenarios

| Scenario ID | Scenario | Priority |
|---|---|---|
| SC-001 | User logs in with valid standard user credentials | High |
| SC-002 | Locked-out user is prevented from logging in | High |
| SC-003 | Invalid username and password show an error message | High |
| SC-004 | Empty login form shows required field validation | Medium |
| SC-005 | Username entered without password shows validation | Medium |
| SC-006 | Password entered without username shows validation | Medium |

## Product Inventory Scenarios

| Scenario ID | Scenario | Priority |
|---|---|---|
| SC-007 | Products page loads after successful login | High |
| SC-008 | Product names, images, prices, and buttons are visible | High |
| SC-009 | User can open product details page | Medium |
| SC-010 | User can return from product details to product list | Medium |

## Sorting Scenarios

| Scenario ID | Scenario | Priority |
|---|---|---|
| SC-011 | Products can be sorted by name A to Z | Medium |
| SC-012 | Products can be sorted by name Z to A | Medium |
| SC-013 | Products can be sorted by price low to high | Medium |
| SC-014 | Products can be sorted by price high to low | Medium |

## Cart Scenarios

| Scenario ID | Scenario | Priority |
|---|---|---|
| SC-015 | User can add one item to cart | High |
| SC-016 | Cart badge updates after adding item | High |
| SC-017 | User can add multiple items to cart | High |
| SC-018 | User can remove item from cart on products page | High |
| SC-019 | User can remove item from cart page | High |
| SC-020 | Cart retains selected items after navigation | Medium |

## Checkout Scenarios

| Scenario ID | Scenario | Priority |
|---|---|---|
| SC-021 | User can start checkout with cart item | High |
| SC-022 | Checkout requires first name | High |
| SC-023 | Checkout requires last name | High |
| SC-024 | Checkout requires postal code | High |
| SC-025 | User can continue to checkout overview with valid information | High |
| SC-026 | Checkout overview displays item, price, tax, and total | High |
| SC-027 | User can complete order successfully | High |

## Logout Scenarios

| Scenario ID | Scenario | Priority |
|---|---|---|
| SC-028 | User can open side menu | Medium |
| SC-029 | User can log out successfully | High |
| SC-030 | User cannot access inventory page after logout without logging in again | High |
