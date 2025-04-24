fruit = input("Which fruit are you eating, banana Or apple?!: ")
color = input("What color is your fruit, green? yellow? brown?")

if fruit == "banana" or fruit == "apple":
    if color == "green":
        print("Your Fruit is unripe")
    elif color == "yellow":
        print("Your Fruit is ripe")
    elif color == "brown":
        print("Your Fruit is overripe")