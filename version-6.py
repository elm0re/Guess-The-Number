import random as rd
import os

play = True
games_played = 0
games_won = 0

while play:

  magic_number = rd.randint(1, 100)
  # print(magic_number)
  
  guess = int(input("Guess a number between 1 and 100:"))
  counter = 10
  os.system("clear")
   
  while guess != magic_number and counter > 0:
    if guess > magic_number:
      print("Guess is too high")
    elif guess < magic_number:
      print("Guess is too low")
    counter-= 1
    print("You lose!")
    print("%s guesses remain." % (counter))
    print("")
    if counter == 0:
      break
    else:
      guess = int(input("Guess a number between 1 and 100:"))
      os.system("clear")
  
  if guess == magic_number:
    print("You win!")
    games_won += 1
  games_played += 1
  
  print("SCOREBOARD")
  print("==========")
  print("Games Won: %s" % games_won)
  print("Games Played: %s" % games_played)
  
  response = input("Would you like to play again? (y/n)")
  os.system("clear")
  if response == "y":
    play = True
  else:
    play = False
