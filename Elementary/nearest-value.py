"""
Найдите ближайшее значение к переданному.
Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.
Нример, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9. Если
отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7,
значит правильный ответ 10.
Несколько уточнений:    Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
    Ряд чисел всегда не пустой, т.е. размер >= 1;
    Переданное значение может быть в этом ряде, а значит оно и является ответом;
    В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
    Ряд не отсортирован и состоит из уникальных чисел.
Input: Два аргумента. Ряд значений в виде set. Искомое значение - int
Output: Int.
"""


def nearest_value(values: set, one: int) -> int:
    # print([(abs(one - value), value) for value in values])
    return min(((abs(one - value), value) for value in values))[1]


print(nearest_value({4, 7, 10, 11, 12, 17}, 9))  # 10
print(nearest_value({4, 7, 10, 11, 12, 17}, 8))  # 7
print(nearest_value({4, 8, 10, 11, 12, 17}, 9))  # 8
print(nearest_value({4, 9, 10, 11, 12, 17}, 9))  # 9
print(nearest_value({4, 7, 10, 11, 12, 17}, 0))  # 4 !!!!
print(nearest_value({4, 7, 10, 11, 12, 17}, 100))  # 17
print(nearest_value({5, 10, 8, 12, 89, 100}, 7))  # 8
print(nearest_value({5, 10, 8, 12, 89, 100}, 100))  # 100
print(nearest_value({-1, 2, 3}, 0))  # -1
