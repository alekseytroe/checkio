import numpy as np


def checkio(numbers_array):
    return sorted(numbers_array, key=abs)


some_list = list(np.random.randint(-10, high=100, size=10))
print(some_list)
print(checkio(some_list))
