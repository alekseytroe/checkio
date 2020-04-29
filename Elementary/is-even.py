"""
Check is the given number is even or not. Your function shoudl return True if the number is even, and False if the
number is odd.
Input: Int.
Output: Bool.
Precondition: both given ints should be between -1000 and 1000
"""


def is_even(num: int) -> bool:
    return num % 2 == 0


print(is_even(2))  # True
print(is_even(5))  # False
print(is_even(0))  # True
