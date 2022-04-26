import random

roll = random.randint(1, 6)
guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("Right! The computer rolled a " + str(roll))

print("Computer rolled a " + str(roll))


