decimal = int(input("Enter the decimal value for conversion: "))

hex = hex(decimal).lstrip("0x")

print("The equivalent hexadecimal value is: ", hex)