print("\nGuesses the answer between 1 to 100\n")

number = 20

trail = 1

while trail <= 5:

    x = int(input("Enter the number :- "))

    if x == number:
        print("\nYou guesses the right")
        break
    elif (x >= 15) and (x <= 19):
        print("Closer\n")
    else:
        print("Try again\n")

    i = i + 1

if trail > 5:
    print("[you loose]")
else:
    print("[you have won]")