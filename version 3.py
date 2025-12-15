import random

def get_user_choice():
  return input("Choose rock, paper, or scissors:")


def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)
  
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "it's a tie!"
  elif user_choice == "rock" and computer_choice == "scissors":
    return "you win!"
  elif user_choice == "paper" and computer_choice == "rock":
    return "you win!"
  elif user_choice == "scissors"  and computer_choice =="paper":
    return "you win!"
  else:
    return "you lose!"
