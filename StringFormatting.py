#have to use str() to format to string
age = 24
print("My age is " + str(age) + " years")

#another way of formatting
print("My age is  {0} years".format(age))

#formatting multiple numbers to strings
print("There are {0} days in {1}, {2}, {3} and {4}".format(31, "January", "March", "May", "July"))

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))