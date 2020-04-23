def checkio(array):
    return sum(array[0::2]) * array[-1] if array else 0


print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))
print(checkio([6]))
print(checkio([]))

