"""Написати скрипт, який конкатенує всі елементи в списку і виведе 
    їх на екран. Список можна "захардкодити".
    Елементами списку повинні бути як рядки, так і числа."""

chek_list = ['морква', 'картошка', 3, 1, 6]
def concatenate_list_data(list):
    result = ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data(['морква', 'картошка', 3, 1, 6]))