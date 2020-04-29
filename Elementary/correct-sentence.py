"""На вход Вашей функции будет передано одно предложение. Необходимо вернуть его исправленную копию так,
чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку, то добавлять
еще одну не нужно, это будет ошибкой
Входные аргументы: Строка (A string).
Выходные аргументы: Строка (A string).
Предусловия: В начале и конце нет пробелов, текст состоит только из пробелов, a-z A-Z , и .
"""


def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    return text[0].upper() + text[1:] + ('.' if text[-1] != '.' else '')


print(correct_sentence("greetings, friends"))  # "Greetings, friends."
print(correct_sentence("Greetings, friends"))  # "Greetings, friends."
print(correct_sentence("Greetings, friends."))  # "Greetings, friends."
print(correct_sentence("hi"))  # "Hi."
print(correct_sentence("welcome to New York"))  # "Welcome to New York."
