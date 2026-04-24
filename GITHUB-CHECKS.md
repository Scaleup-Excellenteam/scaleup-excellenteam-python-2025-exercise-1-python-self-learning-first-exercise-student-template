# GitHub Checks — Pylint, Pytest & CI/CD

Every time you open or update a pull request, two automated checks run on your code:
**Pylint** and **Pytest**. This document explains what they are, why they matter, and
what to do when they fail.

---

## What is CI/CD?

**CI (Continuous Integration)** means that every time you push code, a set of automated
checks runs automatically on GitHub. You do not need to trigger them manually — they
run on their own when you open or update a pull request.

In this course, the CI pipeline runs two checks: Pylint and Pytest.
You can see their results in the **"Checks"** tab of your pull request on GitHub.

> The configuration lives in `.github/workflows/`. Do not modify those files.

---

## Pylint

**Pylint** is a static analysis tool that reads your code without running it and checks
for style violations, bad practices, and potential bugs.

### What it checks

- PEP-8 style conventions (spacing, naming, line length, etc.)
- Missing or malformed docstrings
- Unused variables and imports
- Common logic errors

### How to run it locally

```bash
pip install pylint
pylint $(git ls-files '*.py')
```

### What to do when it fails

1. Read the error output — each line tells you the file, line number, and what is wrong.
2. Fix the issues in your code.
3. Push the fix to your branch — the check will re-run automatically.

A common example:

```
src/5.1.thats_the_way.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
```

This means line 10 of that file is missing a docstring. Add one and push again.

---

## Pytest

**Pytest** is a testing framework. The repository includes pre-written tests in the
`tests/` directory. These tests verify that your functions produce the correct output.

### How to run tests locally

```bash
pip install pytest
pytest
```

To run a single test file:

```bash
pytest tests/test_5_1_thats_the_way.py
```

### What to do when a test fails

1. Read the failure output — pytest shows the expected value vs. what your function returned.
2. Fix your function logic.
3. Re-run the test locally until it passes.
4. Push your fix — the check will re-run on GitHub automatically.

A common example:

```
FAILED tests/test_5_1_thats_the_way.py::test_basic - AssertionError: assert 'hello' == 'Hello'
```

This means your function returned `'hello'` but the test expected `'Hello'`.

---

## Checks only run on `feat/` and `fix/` branches

The CI checks are configured to run **only** when the branch name starts with `feat/`
or `fix/`. If your branch is named differently (e.g. `exercise1`), the checks will not
run. Follow the naming convention from `WORK-INSTRUCTIONS.md`.

---

## Summary

| Check  | What it does                        | Affects grade |
|--------|-------------------------------------|---------------|
| Pylint | Verifies code style and quality     | Yes           |
| Pytest | Verifies your functions are correct | Yes           |

Both checks must pass before your pull request can be considered complete.
