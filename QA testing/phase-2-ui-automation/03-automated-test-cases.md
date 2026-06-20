# Automated UI Test Cases - Phase 2

| Test Case ID | Test File | Scenario | Expected Result | Status |
|---|---|---|---|---|
| AUT-001 | `test_login.py` | Valid login with standard user | Inventory page loads successfully. | Ready |
| AUT-002 | `test_login.py` | Locked-out user login | Locked-out error message is displayed. | Ready |
| AUT-003 | `test_login.py` | Invalid credentials | Invalid login error message is displayed. | Ready |
| AUT-004 | `test_login.py` | Empty login form | Username required error is displayed. | Ready |
| AUT-005 | `test_login.py` | Username without password | Password required error is displayed. | Ready |
| AUT-006 | `test_login.py` | Password without username | Username required error is displayed. | Ready |
| AUT-007 | `test_inventory.py` | Products page loads after login | Product list and product data are visible. | Ready |
| AUT-008 | `test_inventory.py` | Product details navigation | Product details page opens and user can return to products. | Ready |
| AUT-009 | `test_inventory.py` | Sort A to Z | Product names are sorted A to Z. | Ready |
| AUT-010 | `test_inventory.py` | Sort Z to A | Product names are sorted Z to A. | Ready |
| AUT-011 | `test_inventory.py` | Sort low to high | Product prices are sorted lowest to highest. | Ready |
| AUT-012 | `test_inventory.py` | Sort high to low | Product prices are sorted highest to lowest. | Ready |
| AUT-013 | `test_cart.py` | Add one item to cart | Cart badge shows 1 and button changes to Remove. | Ready |
| AUT-014 | `test_cart.py` | Add multiple items to cart | Cart badge count matches added items. | Ready |
| AUT-015 | `test_cart.py` | Remove item from products page | Cart badge is removed and button resets. | Ready |
| AUT-016 | `test_cart.py` | View cart item | Cart page displays selected item. | Ready |
| AUT-017 | `test_cart.py` | Remove item from cart page | Cart item is removed successfully. | Ready |
| AUT-018 | `test_cart.py` | Continue shopping | User returns to products page. | Ready |
| AUT-019 | `test_checkout.py` | Start checkout | Checkout information page opens. | Ready |
| AUT-020 | `test_checkout.py` | Valid checkout information | Checkout overview page opens. | Ready |
| AUT-021 | `test_checkout.py` | Complete order | Success message is displayed. | Ready |
| AUT-022 | `test_checkout.py` | Cancel checkout | User returns to cart. | Ready |
| AUT-023 | `test_checkout.py` | Missing first name | First name required error is displayed. | Ready |
| AUT-024 | `test_checkout.py` | Missing last name | Last name required error is displayed. | Ready |
| AUT-025 | `test_checkout.py` | Missing postal code | Postal code required error is displayed. | Ready |
| AUT-026 | `test_checkout.py` | Special characters in checkout fields | Application handles input without breaking. | Ready |
| AUT-027 | `test_session_and_navigation.py` | Logout | User returns to login page. | Ready |
| AUT-028 | `test_session_and_navigation.py` | Direct inventory access without login | Access is blocked and login page is shown. | Ready |
| AUT-029 | `test_session_and_navigation.py` | Direct cart access without login | Access is blocked and login page is shown. | Ready |
| AUT-030 | `test_session_and_navigation.py` | Direct checkout access without login | Access is blocked and login page is shown. | Ready |
| AUT-031 | `test_session_and_navigation.py` | Access inventory after logout | Access is blocked after logout. | Ready |
