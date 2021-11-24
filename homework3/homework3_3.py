""" Написати функцiю season, 
яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року,
 якiй цей мiсяць належить (зима, весна, лiто або осiнь)"""

month = input("Input the month (e.g. 1,2,3...12 etc.): ")

if month in ('12', '1', '2'):
    season = 'winter'
elif month in ('3', '4', '5'):
    season = 'spring'
elif month in ('6', '7', '8'):
    season = 'summer'
else:
    season = 'autumn'

print("Season is",season)