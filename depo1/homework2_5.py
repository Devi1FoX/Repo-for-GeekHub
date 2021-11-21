"""Написати скрипт, який видалить пусті елементи із списка. 
    Список можна "захардкодити"."""

def compact(lst):
    return list(filter(None, lst))

spysok = compact([(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []])

print(spysok)
