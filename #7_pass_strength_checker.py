password = input("Enter your password: ")
pass_len = len(password)


if pass_len < 7:
    strength = "Weak af, try harder"
elif pass_len < 11:
    strength = "Okey, it's gonna work"
else:
    strength = "dude, this shit is harder then I expected.."

print(strength)