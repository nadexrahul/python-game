print("\nwelcome gamers")
print("\n[Enter]\n\nS for snake\nG for gun\nW for water ")
import random
list1 = ["s", "w", "g"]
i = 10
user1 = 0
pc1 = 0
n10 = input("\nPress any key to start :- ")
print("\nYou have total 10 chances")
while i >= 0:
    pc = random.choice(list1)
    user = input("\nEnter any of them s, g or w :- ")

    if pc == user:
        print("No one wins")

    elif pc == "s" and user == "w":
        pc1 = pc1 + 1
        print("User Guess :- {} and Pc Guess :- {}".format(user, pc))
        print("Pc Wins")
        print("Pc is point :- {}\n".format(pc1))

    elif pc == "s" and user == "g":
        user1 = user1 + 1
        print("User Guess :- {} and Pc Guess :- {}".format(user, pc))
        print("User Wins")
        print("User is point :- {}\n".format(user1))

    elif pc == "g" and user == "s":
        pc1 = pc1 + 1
        print("User Guess :- {} and Pc Guess :- {}".format(user, pc))
        print("Pc Wins")
        print("Pc is point :- {}\n".format(pc1))

    elif pc == "g" and user == "w":
        user1 = user1 + 1
        print("User Guess :- {} and Pc Guess :- {}".format(user, pc))
        print("User Wins")
        print("User is point :- {}\n".format(user1))

    elif pc == "w" and user == "s":
        user1 = user1 + 1
        print("User Guess :- {} and Pc Guess :- {}".format(user, pc))
        print("User Wins")
        print("User is point :- {}\n".format(user1))

    elif pc == "w" and user == "g":
        pc1 = pc1 + 1
        print("User Guess :- {} and Pc Guess :- {}".format(user, pc))
        print("Pc Wins")
        print("Pc is point :- {}\n".format(pc1))
    else:
        print("\nInvalid input\n")

    print("Chances left {}".format(i))

    i = i - 1

if user1 == pc1:
    print("\nSame score no one wins")
elif user1 > pc1:
    print("\nUser won the game by {} points".format(user1))
elif pc1 > user1:
    print("\nPc won the match by {} points".format(pc1))

n10 = input("Press any key to exit :- ")