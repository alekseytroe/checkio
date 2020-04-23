import re


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    return re.search("[a-zA-Z']+", text).group() if text else 'no words'


print(','.isalpha())
print(first_word("Hello world"))
print(first_word(" a'word "))
print(first_word("don't touch it"))
print(first_word("greetings, friends"))
print(first_word("... and so on ..."))
print(first_word(",hi"))
print(first_word("Hello.World"))
print(first_word(''))