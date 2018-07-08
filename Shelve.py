import shelve

# with shelve.open("ShelveTest") as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow, citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"

#another way adding to shelve file
fruit = shelve.open("ShelveTest")
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow, citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

# print(fruit['lemon'])
# print(fruit['grape'])
#
# fruit['lime'] = "great with tequila"
#
# for snack in fruit:
#     print("{} : {}".format(snack, fruit[snack]))

# while True:
#     shelf_key = input("Please enter a fruit: ")
#     if shelf_key == "quit":
#         break
#
#     description = fruit.get(shelf_key, "We don't have a {}".format(shelf_key))
#     print(description)

#print the shelf:
for f in fruit:
    print(f + "-" + fruit[f])

print('-' * 40)

#print the shelf in order
ordered_keys = list(sorted(fruit.keys()))

for f in ordered_keys:
    print(f + "-" + fruit[f])

fruit.close()

print(fruit)
