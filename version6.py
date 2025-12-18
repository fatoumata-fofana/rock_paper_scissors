import os
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

def get_user_choice():
  valid_choices = ["rock", "paper", "scissors"]
  while True:
    choice = input("Choose rock, paper, or scissors: ").strip().lower()
    if choice in ["rock","paper","scissors"]:
      print("Good choice.")
      return choice
    else:
      print("Invalid choice. Please try again.")


def play_game():
  while True:
    user_choice = get_user_choice()
    os.system("clear")
    computer_choice = get_computer_choice()
    print("User choice: " + user_choice)
    print("Computer choice: " + computer_choice)
    print("")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    print("")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    os.system("clear")
    if play_again == "yes":
      continue
    else:
      print("Thanks for playing!")
    break
  


play_game()
