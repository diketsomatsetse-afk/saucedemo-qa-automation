# SauceDemo QA Automation

![UI tests](https://github.com/diketsomatsetse-afk/saucedemo-qa-automation/actions/workflows/tests.yml/badge.svg)

Automated UI tests for [SauceDemo](https://www.saucedemo.com), a public demo
e-commerce site, written in **Python** with **pytest** and **Playwright**.

The suite covers the main customer journey (login, browsing, cart and checkout)
and documents two real defects found during testing.

## What is tested

| Area | Tests | What they check |
|---|---|---|
| Login | 6 | Valid login, locked-out user, wrong password, required fields, protected pages |
| Products | 5 | Product list loads, sorting by name and price (A–Z, Z–A, low–high, high–low) |
| Cart | 4 | Add, add multiple, remove, cart kept after page reload |
| Checkout | 5 | Full purchase, subtotal/tax/total maths, form validation |
| Known bugs | 2 | Defects reproduced as `xfail` tests (see [bug reports](docs/bug-reports.md)) |

**Result:** 20 passed, 2 expected failures (known bugs).

## Approach

- **Page Object Model.** Each screen has a class in `pages/` that holds its
  locators and actions, so tests read like user steps and a UI change only
  needs fixing in one place.
- **Stable locators.** Elements are found by `data-test` attributes rather than
  CSS styling, which makes tests less brittle.
- **Data-driven tests.** `pytest.mark.parametrize` runs one test against many
  inputs (e.g. every sort option, every required field).
- **Known bugs as `xfail(strict=True)`.** The suite stays green while a bug
  exists and alerts the team when it is fixed.
- **Continuous integration.** GitHub Actions runs every test on each push and
  saves an HTML report.

## Project structure

```
pages/           Page objects (login, inventory, cart, checkout)
tests/           Test files, one per feature area
docs/            Bug reports
conftest.py      Shared fixtures and test accounts
.github/         CI workflow
```

## Run it yourself

Requires Python 3.12.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
python -m playwright install chromium

pytest                          # run everything
pytest -m smoke                 # quick smoke tests only
pytest --headed                 # watch the browser
pytest --html=report.html       # HTML report
```

## Author

**Diketso Matsetse** · QA Analyst ·
[LinkedIn](https://linkedin.com/in/diketso-akanyang-matsetse-ab680391)
