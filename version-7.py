import os
import random


def get_user_choice():
  valid_choices = ["rock", "paper", "scissors"]
  while True:
    choice = input("Choose rock, paper, or scissors: ").strip().lower()
    if choice in ["rock","paper","scissors"]:
      print("Good choice.")
      return choice
    else:
      print("Invalid choice. Please try again.")

def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  return random.choice(choices)
  
def determine_winner(user_choice, computer_choice, user_score, cpu_score, ties):
  if user_choice == computer_choice:
    return "it's a tie!", user_score, cpu_score, ties + 1
  elif user_choice == "rock" and computer_choice == "scissors":
    return "you win!", user_score + 1, cpu_score, ties
  elif user_choice == "paper" and computer_choice == "rock":
    return "you win!", user_score + 1, cpu_score, ties
  elif user_choice == "scissors"  and computer_choice =="paper":
    return "you win!", user_score + 1, cpu_score, ties
  else:
    return "you lose!", user_score, cpu_score + 1, ties

def show_score(user_score, cpu_score, ties):
  print("SCOREBOARD:")
  print("-----------")
  print("Wins: %s" % user_score)
  print("Losses: %s" % cpu_score)
  print("Ties: %s" % ties)
  print("")

def play_game():
  user_score = 0
  cpu_score = 0
  ties = 0
  while True:
    user_choice = get_user_choice()
    os.system("clear")
    computer_choice = get_computer_choice()
    print("User choice: " + user_choice)
    print("Computer choice: " + computer_choice)
    print("")
    result, user_score, cpu_score, ties = determine_winner(user_choice, computer_choice, user_score, cpu_score, ties)
    print(result)
    print("")
    show_score(user_score, cpu_score, ties)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    os.system("clear")
    if play_again == "yes":
      continue
    else:
      print("Thanks for playing!")
    break

play_game()
