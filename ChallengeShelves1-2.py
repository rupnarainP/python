import shelve

# #splits the dicationary into a list containing 10 words
# print(locations[0].split())
# #uses the comma as a delimeter to split words into a list
# print(locations[3].split(","))
# #can split each word and display it
# print(" ".join(locations[0].split()))

#starting point
loc = "1"

locations = shelve.open("locations")
vocabulary = shelve.open("vocabulary")

while True:
    availableExits = locations[loc]["exits"].keys()

    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    print(locations[loc]['desc'])

    if loc == "0":
        break;

    direction = input("The available exits are: {} ".format(availableExits.upper()))
    print()

    if len(direction) > 1:
        words = direction.split()

        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                print(vocabulary[word])

    else:
        if direction in locations[loc]:
            loc = locations[loc][direction]

        else:
            print("You cannot go in that direction")

locations.close()
vocabulary.close()