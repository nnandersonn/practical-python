import random

computer_choice = random.choice(['Scissors', 'Rock', 'Paper'])

user_choice = input('Do you want: Rock, Paper, or Scissors?\n')



if computer_choice == user_choice:
    print("Tie")
elif computer_choice == 'Scissors' and user_choice == "Rock":
    print("Win")
elif computer_choice == "Rock" and user_choice == "Paper":
    print("Win")
elif computer_choice == "Paper" and user_choice == "Scissors":
    print("Win")
else:
    print("Lose")