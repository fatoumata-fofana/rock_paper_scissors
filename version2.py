import random

def get_user_choice():
  return input("Choose rock, paper, or scissors:")


def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)

get_user_choice()
