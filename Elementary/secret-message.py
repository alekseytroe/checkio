"""
Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.
Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим
сообщение "HELLO".
Входные данные: Текст как строка (юникод).
Выходные данные: Секретное сообщение как строка или пустая строка.
Предусловие: 0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)
"""


def find_message(text):
    return ''.join(symbol for symbol in text if symbol.isupper())


print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))  # "HELLO", "hello"
print(find_message("hello world!"))  # "", "Nothing"
print(find_message("HELLO WORLD!!!"))  # "HELLOWORLD", "Capitals"
