""" Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят
только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one
two three 7 end" есть три слова подряд.
Входные данные: Строка со словами (str).
Выходные данные: Ответ как логическое выражение (bool), True или False.
Предусловия: Исходная строка содержит только слова и/или числа. Смешанных слов нет (перемешанные цифры и буквы).
0 < len(words) < 100 """


def checkio(words):
    return 'True,True,True' in ','.join(str(word.isalpha()) for word in words.split())


print(checkio("Hello World hello"))
print(checkio("He is 123 man"))
print(checkio("1 2 3 4"))
print(checkio("bla bla 1 h bla bla"))

