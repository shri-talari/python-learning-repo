'''Q2. Password Strength Checker

Write a program that asks the user to enter a password and checks if it is strong using regex rules:

Minimum 8 characters

At least one uppercase letter

At least one lowercase letter

At least one digit

At least one special character (@, #, $, %, &, *)

If password fails, raise an exception and show which rule(s) are violated.'''

import re


def check_password_strength(password):
    violations = []

    if len(password) < 8:
        violations.append("Password must be at least 8 characters long.")

    if not re.search(r'[A-Z]', password):
        violations.append(
            "Password must contain at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        violations.append(
            "Password must contain at least one lowercase letter.")

    if not re.search(r'\d', password):
        violations.append("Password must contain at least one digit.")

    if not re.search(r'[@#$%&*]', password):
        violations.append(
            "Password must contain at least one special character (@, #, $, %, &, *).")

    if violations:
        raise ValueError("\n".join(violations))
    else:
        print("Password is strong.")


password = input("Enter your password: ")
try:
    check_password_strength(password)
except ValueError as e:
    print("Password is not strong enough:")
    print(e)
