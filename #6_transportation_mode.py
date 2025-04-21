distance = int(input("Distance in Kilometer: "))

if distance <= 1:
    transport = "Just walk dude.."
elif distance <= 15:
    transport = "You've bike right? use that.."
else:
    transport = "You got no car right? then book a taxi..!"

print("Transport mode suggetion: ", transport)