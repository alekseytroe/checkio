"""
You have a number and you need to determine which digit in this number is the biggest.
Input: A positive int.
Output: An Int (0-9).
"""


def max_digit(number: int) -> int:
    return int(max(str(number)))


print(max_digit(0))  # 0
print(max_digit(52))  # 5
print(max_digit(634))  # 6
print(max_digit(1))  # 1
print(max_digit(102000))  # 1
