import random

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
game_images=[rock, paper, scissors]
human_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper,"
            "or 2 for Scissors\n"))
if human_choice>=0 and human_choice<=2:
    print(game_images[human_choice])
computer_choice=random.randint(0,2)
print(f"Computer chose:\n {game_images[computer_choice]}")
if human_choice >= 3 or human_choice < 0:
    print("You typed and invalid number. You lose!")
elif human_choice>computer_choice:
    print("You win!")
elif human_choice<computer_choice:
    print("You lose!")
elif human_choice==0 and computer_choice==2:
    print("You win!")
elif human_choice==2 and computer_choice==0:
    print("You lose! ")
elif human_choice==computer_choice:
    print("It's a draw!")
