"""Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно)."""
nl = []

a = int(input("Enter some year: "))
b = int(input("Enter some year: "))

for x in range(a, b):
    if(((x%4==0) and (x%100!=0)) or (x%400==0)):
        nl.append(str(x))
print (','.join(nl))