"""In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a
word it shouldn't be counted. The text consists from numbers, spaces and english letters Input: A string. Output: An
int. """


def sum_numbers(text: str) -> int:
    return sum([int(x) for x in text.split() if x.isnumeric()])


print(sum_numbers('hi'))  # 0
print(sum_numbers('who is 1st here'))  # 0
print(sum_numbers('my numbers is 2'))  # 2
print(sum_numbers('This picture is an oil on canvas '
                  'painting by Danish artist Anna '
                  'Petersen between 1845 and 1910 year'))  # 3755
print(sum_numbers('5 plus 6 is'))  # 11
print(sum_numbers(''))  # 0
