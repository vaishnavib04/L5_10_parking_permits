# Static Analysis Issue Documentation

## 1. Overview

The parking permit management program was analyzed using Pylint, Bandit, and Flake8. These tools were used to identify code-quality problems, potential security risks, and Python style violations. The findings were addressed, and the tools were run again to verify the corrections.

## 2. Issue Documentation Table

| No. | Issue Identified | Tool | Correction Applied | Outcome |
|---|---|---|---|---|
| 1 | Missing module and function docstrings. | Pylint | Added descriptive documentation to the module and functions. | Improved code documentation and readability. |
| 2 | Mutable default argument in `register_permit()`. | Pylint | Changed the default argument to `None` and initialized the list inside the function. | Avoided sharing a mutable default list between calls. |
| 3 | Bare `except` clauses. | Pylint and Flake8 | Replaced bare exception handlers with appropriate specific exception types. | Improved error handling and removed the reported violations. |
| 4 | Permit numbers generated using `random.randint()`. | Bandit | Replaced the `random` module with `secrets` for generating permit numbers. | Eliminated the B311 security warning. |
| 5 | Lines exceeding the permitted line length. | Pylint and Flake8 | Split long statements across multiple lines. | Removed the reported line-length violations. |
| 6 | Incorrect blank-line spacing around functions. | Flake8 | Corrected blank-line spacing to follow Python style conventions. | Removed the reported spacing violations. |
| 7 | Function name `setExpiry` did not follow the recommended naming convention. | Pylint | Renamed the function to `set_expiry`. | Followed the recommended snake_case naming convention. |
| 8 | File operations lacked explicit encoding and appropriate resource management. | Pylint | Specified UTF-8 encoding and used context managers for file operations. | Improved file handling and resource management. |
| 9 | Use of a global statement. | Pylint | Refactored the relevant code to avoid an unnecessary global statement. | Improved code organization. |

## 3. Before-and-After Results

| Tool | Before Correction | After Correction |
|---|---|---|
| Pylint | Score: 6.32/10 | Score: 10.00/10 |
| Bandit | One low-severity B311 finding | No issues identified |
| Flake8 | 16 reported violations | No reported violations |

## 4. Summary

Pylint helped identify maintainability and code-quality issues, Bandit identified the use of an unsuitable random number generator for security-sensitive permit number generation, and Flake8 identified formatting and style violations.

After the corrections, the program achieved a Pylint score of 10.00/10, Bandit reported no issues, and Flake8 reported no remaining violations. The before-and-after reports provide evidence of the analysis and improvements.