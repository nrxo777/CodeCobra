age = int(input("Enter your age: "))
day = input("Enter the day of show: ")

price = 550 if age >= 20 else 450
if day == "wednesday":
    price -= 20

print("The ticket price is TK.", price)