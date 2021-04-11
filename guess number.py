print("you have 5 trails to guess the number")
trail = 1
while trail <= 5:
    x = int(input("enter the number "))

    if x == 10:
        break
    elif (x >= 5) and (x <= 15):
        print("you are close")

    trail = trail + 1
    print("try again")

if x == 10:
    print("you won")
else:
    print("you lost")