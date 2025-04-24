input_str = input("Enter a keyword: ")

for char in input_str:
    if input_str.count(char) == 1:
        print("The Character is: ", char)
        break