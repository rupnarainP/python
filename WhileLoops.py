# i = 0
#
# while i < 10:
#     print("i is now: {}".format(i))
#     i += 1

availableExits = {"east", "north east", "south"}

chosenExit = ""

while chosenExit not in availableExits:
    print(availableExits)
    chosenExit = input("Please choose a direction: ")

    if chosenExit == "quit":
        print("Game Over!")
        break

#can use this else statement with the loop so if you break out of the loop, te message isn't displayed
else:
    print("Aren't you glad you got out of there?")
