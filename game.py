import random

total_guesses = 0
guessed_number = 0
random_number = random.randint(1, 100)
print('random number is ', random_number)
name = input("Hello, what is your name? ")
print(name + ", I am thinking of a number between 1 and 100.\nTry to guess my number")

while True:
    guessed_number = int(input("Your guess? "))
    total_guesses += 1
    if guessed_number > random_number:
        print("Your guess is too high. Try again.")
    elif guessed_number < random_number:
        print("Your guess is too low. Try again.")
    else:
        print("Well done, " + name + "! you found my number in " + str(total_guesses) +" tries!")
        break
