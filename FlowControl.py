#if statements
# name = input("Please enter your name ")
# age = int(input("How old are you {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You're old enough to vote")
#     print("Please put an x in the box")
# else:
#     print("Please come back in {0} years".format(18-age))

##############################################################################

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher")
#         guess = int(input())
#
#     else:
#         print("Please guess lower")
#         guess = int(input())
#
#     if guess == 5:
#         print("Correct")
#
#     else:
#         print("Sorry")
#
# else:
#     print("Well done, you've guessed it on the first try!")

#################################################################################


age = int(input("How old are you? "))

if (age >= 16) and (age <= 65):
    print("Have a good day at work")