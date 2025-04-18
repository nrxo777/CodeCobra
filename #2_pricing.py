age = int(input("Enter your age: "))
day = input("Enter the day of show: ")

if age <= 0:
    print("Input a valid age sir..!")
elif age <= 13 and day == "wednesday":
    print("Ticket price is Tk. 450 but today you got for Tk. 410")
elif age <= 13:
    print("The movie ticket price is Tk. 450")
elif age <= 59 and day == "wednesday":
    print("Ticket price is Tk. 550 but today you got for Tk. 490")
elif age <= 59:
    print("Your ticket price is Tk. 550")
else:
    print("damn dude!! just go inside and watch the movie for free...")

