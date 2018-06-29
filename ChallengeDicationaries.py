locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "you are inside a building, a well house for a small stream",
             4: "You are in a valley besides a stream",
             5: "You are in the forest"}

# exits = [{"Q": 0}, #Quit
#          {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0}, #at the Road
#          {"N": 5, "Q": 0}, #at the Hill
#          {"W": 1, "Q": 0}, #at the Building
#          {"N": 1, "W": 2, "Q": 0}, #at the Valley
#          {"W": 2, "S": 1, "Q": 0}] #at the Forest

exits = {0: {"Q": 0}, #Quit
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0}, #at the Road
         2: {"N": 5, "Q": 0}, #at the Hill
         3: {"W": 1, "Q": 0}, #at the Building
         4: {"N": 1, "W": 2, "Q": 0}, #at the Valley
         5: {"W": 2, "S": 1, "Q": 0}} #at the Forest

keyWords = {"NORTH": "N",
            "EAST": "E",
            "SOUTH": "S",
            "WEST": "W",
            "QUIT": "Q"}

# #splits the dicationary into a list containing 10 words
# print(locations[0].split())
# #uses the comma as a delimeter to split words into a list
# print(locations[3].split(","))
# #can split each word and display it
# print(" ".join(locations[0].split()))

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

    if len(direction) > 1:
        words = direction.split()

        for word in words:
            if word in keyWords:
                direction = keyWords[word]
                print(keyWords[word])

    else:
        if direction in exits[loc]:
            loc = exits[loc][direction]

        else:
            print("You cannot go in that direction")


