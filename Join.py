# myList = ["a", "b", "c", "d"]
#
# #don't need a loop to add the characters of the list to the string
# newString = ", ".join(myList)
# print(newString)
#
# letters = "abcdefghijklmnopqrstuvwxyz"
# numbers = "123456789"
#
# newString = " mississippi ".join(numbers)
# print(newString)

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "you are inside a building, a well house for a small stream",
             4: "You are in a valley besides a stream",
             5: "You are in the forest"}

exits = [{"Q": 0}, #Quit
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0}, #at the Road
         {"N": 5, "Q": 0}, #at the Hill
         {"W": 1, "Q": 0}, #at the Building
         {"N": 1, "W": 2, "Q": 0}, #at the Valley
         {"W": 2, "S": 1, "Q": 0}] #at the Forest

#starting point
loc = 1

while True:
    availableExits = ", ".join(exits[loc].keys())

    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break;

    direction = input("The available exits are: {} ".format(availableExits.upper()))
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]

    else:
        print("You cannot go in that direction")
