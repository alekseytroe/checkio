""" In this mission you need to create a password verification function.
Those are the verification conditions: the length should be bigger than 6.
"""


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6

