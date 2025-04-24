age = int(input("Please enter your age: "))

if age < 0:
    print("Just born already...")
elif age == 0:
    print("You just born, chill")
elif age < 13:
    print("You're a child. go home and watch Naruto.")
elif age < 20:
    print("You're a teenager, start fighting with friends.")
elif age < 59:
    print("You're a mature, get a job dude.")
elif age == 100:
    print("You just hit the century club!")
elif age < 101:
    print("You're a senior, you did great.")
elif age < 169:
    print("You're fukking old. How's the 18th century?")
else:
    print("You know what, you're ancient.. like a dinosaur.")