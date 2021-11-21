some_number = int(input('Write your number: '))
result = ""

for a in range(some_number):
    print(a)
    user_text = input('Write your text:')
    result = result + user_text
print(result)