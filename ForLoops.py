for i in range(1, 20):
    print("i is now: {0}".format(i))

number = "9, 12, 33, 3, 5"

# for i in range(0, len(number) -1):
#     print(number[i])
#

cleanedNumber = ''
# converting to integer
for i in range(0, len(number) - 1):
    if number[i] in "0123456789":
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print(newNumber)

# can write it on one line
for i in range(0, len(number) - 1):
    if number[i] in "0123456789":
        print(number[i], end='')

for char in number:
    if char in "0123456789":
        cleanedNumber += char

newNumber = int(cleanedNumber)
print("New number is {0}".format(newNumber))

for state in ["not pinin", "no more", "a stiff"]:
    print("This parrot is " + state)

#for loop with step
for i in range(0, 100, 5):
    print("i is {0}".format(i))


for i in range(1, 13):
    for j in range(1, 13):
        print("{0} * {1} = {2}".format(i, j, i*j), end='')
        print()
