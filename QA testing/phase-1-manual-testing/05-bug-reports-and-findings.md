# Bug Reports and Findings - Phase 1

## Summary

No confirmed bugs were found during Phase 1 manual UI testing.

All planned manual test cases and negative/edge test cases passed during execution. Login, inventory, sorting, cart, checkout, logout, session access, and validation behavior worked according to the expected results.

## Bug Summary

| Bug ID | Feature | Summary | Severity | Status |
|---|---|---|---|---|
| N/A | N/A | No confirmed bugs found during this phase. | N/A | N/A |

## Observations

| Observation ID | Area | Observation | Status |
|---|---|---|---|
| OBS-001 | Problem User | The `problem_user` account was reviewed for visual or workflow inconsistencies. The application remained usable during testing. | Documented |
| OBS-002 | Performance Glitch User | The `performance_glitch_user` account showed slower login/page loading behavior. This was documented as expected behavior for that test user. | Documented |
| OBS-003 | Empty Cart Checkout | The application handled the empty cart checkout flow consistently without breaking. | Documented |
| OBS-004 | Session Protection | Direct access to cart and checkout pages after logout was blocked or redirected appropriately. | Documented |

## Conclusion

Phase 1 manual testing did not identify any confirmed defects. The tested workflows behaved as expected, and all manual, negative, and edge test cases passed.