# Функция должна распознавать является ли тема письма стрессовой. Стрессовая тема определяется тем, что все буквы в
# верхнем регистре, и / или заканчиваются как минимум тремя восклицательными знаками, и / или содержат по крайней
# мере одно из следующих слов-маркеров: "help", "asap", "urgent". Любое из этих слов-маркеров может быть написано
# по-разному: «HELP», «help», «HeLp», «H! E! L! P!», «H-E-L-P», и даже очень непринужденно «HHHEEEEEEEEELLP».
# Входные данные: Тема письма в виде строки.
# Выходные данные: Boolean.
# Предварительное условие: Тема может содержать до 100 букв.
import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    find = re.findall('(H+[!\s]E+[!\s]L[!\s]+[!\s]P+[!\s])', subj)
    print(find, len(find))
    return find



is_stressful('giv my H! E! L! P!')
is_stressful('HHEELPPP')
is_stressful('help')
is_stressful('Help')
