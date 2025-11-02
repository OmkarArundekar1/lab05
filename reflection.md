
---

## 🪶 **reflection.md**

```markdown
# Reflection — Lab 5: Static Code Analysis

---

### 1️⃣ What issues did you identify and fix?

I identified and fixed six major issues in the original `inventory_system.py`:
1. **Mutable default arguments** (`logs=[]`) — replaced with `None` to avoid shared state.
2. **Missing input validation** — prevented crashes when invalid types were passed.
3. **Bare `except:` blocks** — replaced with specific exception types.
4. **Unsafe `eval()` usage** — replaced with `ast.literal_eval()` to remove security risks.
5. **Improper file handling** — converted to use `with open()` for safe file I/O.
6. **Lack of logging** — added structured logging for better debugging and clarity.

---

### 2️⃣ Which issues were easiest or hardest to fix?

- **Easiest:** Style errors flagged by Flake8, such as missing blank lines and spacing.
- **Hardest:** Replacing `eval()` safely with `ast.literal_eval()` while preserving similar functionality.

---

### 3️⃣ Did you find any false positives or low-severity issues?

Yes.  
- Pylint flagged the use of a global variable (`stock_data`) and non-conventional function names (like `addItem`), but they were intentional for the script’s design.
- Bandit gave minor warnings about general exception handling, which were acceptable after adding logging.

---

### 4️⃣ How could static analysis be integrated into CI/CD pipelines?

By adding a **GitHub Actions workflow** that automatically runs `pylint`, `flake8`, and `bandit` on every push or pull request.  
This ensures all future commits maintain the same security and style standards.  
It prevents regressions and encourages continuous code quality improvement.

---

### 5️⃣ What did you learn?

I learned how static analysis tools help detect logic, security, and style issues early — even before testing.  
Using Pylint, Bandit, and Flake8 together provides full coverage across code quality, security, and readability.  
This lab showed that **automation + static analysis = cleaner, safer code**.

---

**Submitted by:** Omkar Arundekar  
**Date:** 2 November 2025  
**Course:** Software Engineering — Lab 5  
