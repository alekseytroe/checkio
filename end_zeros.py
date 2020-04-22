""" Try to find out how many zeros a given number has at the end.
Input: A positive Int
Output: An Int. """


def end_zeros(num: int) -> int:
    count = 0
    for symbol in str(num)[::-1]:
        if symbol == '0':
            count += 1
        else:
            break
    return count


print(end_zeros(0)) #== 1
print(end_zeros(1)) #== 0
print(end_zeros(10)) #== 1
print(end_zeros(101)) #== 0
print(end_zeros(245)) #== 0
print(end_zeros(100100)) #== 2