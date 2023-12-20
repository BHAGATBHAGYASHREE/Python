num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
floor_division = num1 // num2 if num2 != 0 else "Cannot divide by zero!"
modulus = num1 % num2 if num2 != 0 else "Cannot calculate modulus with zero divisor!"
exponentiation = num1 ** num2

bitwise_and = int(num1) & int(num2)
bitwise_or = int(num1) | int(num2)
bitwise_xor = int(num1) ^ int(num2)
left_shift = int(num1) << int(num2)
right_shift = int(num1) >> int(num2)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)