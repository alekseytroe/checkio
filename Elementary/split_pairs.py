"""Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй
символ последней пары должен быть заменен подчеркиванием ('_').
Входные данные: Строка.
Входные данные: An iterable of strings.
Предварительное условие: 0<=len(str)<=100
"""


def split_pairs(a):
    a += '_'
    while len(a) > 1:
        yield a[0:2]
        a = a[2:]


print(list(split_pairs('abcd')))  # ['ab', 'cd']
print(list(split_pairs('abc')))  # ['ab', 'c_']
print(list(split_pairs('abcdf')))  # ['ab', 'cd', 'f_']
print(list(split_pairs('a')))  # ['a_']
print(list(split_pairs('')))  # []
print(list(split_pairs('bb')))  # ['hh']

