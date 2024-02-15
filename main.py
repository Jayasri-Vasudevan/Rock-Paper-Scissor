rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]
print("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user = int(input())
if user >= 3 or user < 0:
    print("Invalid input")
else:
    print(game_images[user])

    print("Computer chose")
    computer = random.randint(0, 2)
    print(game_images[computer])

    if user == 0 and computer == 2:
        print("You win")
    elif user == 2 and computer == 1:
        print("You win")
    elif user == 1 and computer == 0:
        print("You win")
    elif user == 2 and computer == 0:
        print("You lose")
    elif user == 1 and computer == 2:
        print("You lose")
    elif user == 0 and computer == 1:
        print("You lose")
    elif user == 0 and computer == 0:
        print("Tie! Play again")
    elif user == 1 and computer == 1:
        print("Tie! Play again")
    else:
        print("Tie! Play again")
