number = "9, 223, 372, 036, 854, 775, 807"
cleanedNumber = ""

for i in range(0, len(number) - 1):
    if number[i] in "012356789":
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))
