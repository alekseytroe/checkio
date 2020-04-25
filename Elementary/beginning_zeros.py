"""You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of
the given string.
Input: A string, that consist of digits.
Output: An Int.
Precondition: 0-9
"""


def beginning_zeros(number: str) -> int:
    for i, digit in enumerate(number):
        if digit != '0':
            return i
    else:
        return len(number)



print(beginning_zeros('100'))  # 0
print(beginning_zeros('001'))  # 2
print(beginning_zeros('100100'))  # 0
print(beginning_zeros('001001'))  # 2
print(beginning_zeros('012345679'))  # 1
print(beginning_zeros('0000'))  # 4
