score = int(input("Enter your score: "))

if score > 100:
    print("Invalid input..")
    exit()

if score >= 90:
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60:
    print("Your grade is D")
elif score >= 1:
    print("You've failed..")
elif score <= 0:
    print("Invalid input")
else:
    print("Invalid input")