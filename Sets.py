# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("-" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
#
# print(farm_animals)
# print(wild_animals)
#
# #creating an empty set
# empty_set = set()
# empty_set.add("Hello")
# print(empty_set)
#
# #creating an empty dictionary
# empty_set2 = {}
#
# even = set(range(0, 40, 2))
# squares_tuple = (4, 6, 9, 16, 25)
# print(even)
#
# #using tuples to generae a set
# squares = set(squares_tuple)
# print(squares)

# even = set(range(0, 40, 2))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
# print("-" * 40)
#
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

even = set(range(0, 40, 2))
print(sorted(even))

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("Even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even-squares))

print("Squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares-even))