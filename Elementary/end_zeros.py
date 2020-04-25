""" Try to find out how many zeros a given number has at the end.
Input: A positive Int
Output: An Int. """


def end_zeros(num: int) -> int:
    for i, digit in enumerate(str(num)[::-1]):
        if digit != '0':
            return i
    else:
        return len(str(num))


print(end_zeros(0)) #== 1
print(end_zeros(1)) #== 0
print(end_zeros(10)) #== 1
print(end_zeros(101)) #== 0
print(end_zeros(2450)) #== 0
print(end_zeros(100100)) #== 2