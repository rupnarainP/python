import random

highest = 10
answer = random.randint(1, highest)
attempts = "true"

print(answer)
count = 0
guess  = 0

print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:

    guess = int(input())

    if guess < answer:
        print("Please guess higher")
        guess = int(input())

    else:
        print("Please guess lower")
        guess = int(input())

    if guess == answer:
        print("Correct")
        break

    else:
        print("Sorry")