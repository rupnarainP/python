myList = list(range(10))

print(myList)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

print(even)
print(odd)

#finding an index in a string
myString = "abcdefghijklmnop"
print(myString.index("e"))
print(myString[4])

r = range(0, 101)

for i in r[::-2]:
    print(i)

#can reverse a string
rad = "asdf"
print(rad[::-1])