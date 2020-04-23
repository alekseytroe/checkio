"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it -
function should return True.
Precondition: a-z, A-Z, 1-9 and spaces
"""


def is_all_upper(text: str) -> bool:
    return text == text.upper()
    # return False not in [x.isupper() for x in text if x.isalpha()]


print(is_all_upper('ALL UPPER'))  # True
print(is_all_upper('all lower'))  # False
print(is_all_upper('mixed UPPER and lower'))  # False
print(is_all_upper(''))  # True
