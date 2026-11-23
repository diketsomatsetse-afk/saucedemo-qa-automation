# Bug Reports

Defects found while testing [SauceDemo](https://www.saucedemo.com). Each one is
covered by an automated test marked `xfail`, so the suite stays green while the
bug exists and fails loudly if the behaviour changes.

---

## BUG-001: Every product shows the same placeholder image

| Field | Value |
|---|---|
| **Severity** | Medium |
| **Priority** | Medium |
| **Environment** | Chromium (Playwright), https://www.saucedemo.com |
| **Account** | `problem_user` |
| **Test** | `tests/test_inventory.py::test_problem_user_product_images_are_unique` |

**Steps to reproduce**
1. Go to https://www.saucedemo.com
2. Log in as `problem_user` / `secret_sauce`
3. Look at the product images on the Products page

**Expected result:** Each of the 6 products shows its own image, as it does for `standard_user`.

**Actual result:** All 6 products show the same image (`sl-404-*.jpg`, a "not found" placeholder).

**Impact:** Customers cannot see what they are buying, which is likely to reduce sales and increase returns.

---

## BUG-002: Last Name field on checkout does not accept input

| Field | Value |
|---|---|
| **Severity** | High (blocks checkout) |
| **Priority** | High |
| **Environment** | Chromium (Playwright), https://www.saucedemo.com |
| **Account** | `problem_user` |
| **Test** | `tests/test_checkout.py::test_problem_user_can_enter_last_name` |

**Steps to reproduce**
1. Log in as `problem_user` / `secret_sauce`
2. Add "Sauce Labs Backpack" to the cart
3. Open the cart and click **Checkout**
4. Type "User" into the **Last Name** field

**Expected result:** The Last Name field contains "User".

**Actual result:** The Last Name field stays empty after typing.

**Impact:** The customer cannot complete the required checkout form, so the purchase is blocked.
