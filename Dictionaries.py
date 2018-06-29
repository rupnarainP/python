#Does not allow duplicates
#Unordered
#key, value pairs

fruit = {"orange" : "a sweet orange citrus fruit",
         "apple" : "good for making cider",
         "lemon" : "a sour, yellow, citrus fruit",
         "grape" : "a small, sweet fruit growing in bunches",
         "lime" : "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
#
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# #used to delete an item
# del fruit["apple"]
# print(fruit)
#
# #clear the dictionary
# fruit.clear()
# print(fruit)

#to check if the key exists
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break;
#     description = fruit.get(dict_key, "We don't have a {}".format(dict_key))
#     print(description)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("{} does not exist".format(dict_key))

#iterate through keys in a dictionary
# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print("{} is {}".format(snack, fruit[snack]))
#     print("-" * 40)

# #to print in order
# orderedKeys = list(fruit)
# orderedKeys.sort()
#
# for k in orderedKeys:
#     print("{} is {}".format(k, fruit[k]))
#

# #another way of sorting and printing in order
# for f in sorted(fruit.keys()):
#     print("{} is {} ".format(f, fruit[f]))

# #to iterate values of a dicationary but is not efficient, rather use keys
# for v in fruit.values():
#     print("The values are: {}".format(v))

# fruitKeys = fruit.keys()
#
# fruit["tomato"] = "not nice with ice-cream"
# print(fruitKeys)

print(fruit)
#creates a tuple
print(fruit.items())

#can store as a tuple
f_tuple = tuple(fruit.items())
print(f_tuple)

#iterate through the tuple
for item in f_tuple:
    print(item)

#can convert back into a dictionary
print(dict(f_tuple))