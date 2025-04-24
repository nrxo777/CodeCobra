number = int(input("Enter a value: "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1
    
print("Factorial value is", factorial)