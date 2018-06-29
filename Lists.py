#Lists
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

#Concatenating lists
numbers = even + odd

#Sorting lists but does not return a value
numbers.sort()
print(numbers)

#sorted() returns a sorted list
orderedNumbers = sorted(numbers)
print(orderedNumbers)

#creating empty lists
list1 = []
list2 = list()

if list1 == list2:
    print("Equal")

#can input into the list constructor to create a list of characters
print(list("The lists are equal"))

#reversing the list
anotherEven = even
anotherEven.sort(reverse=True)
print(anotherEven)
print(anotherEven is even)