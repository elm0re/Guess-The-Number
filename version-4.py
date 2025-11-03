import random as rd

magic_number = rd.randint(1, 10)
# print(magic_number)

guess = int(input("Guess a number between 1 and 10:"))
counter = 3

while guess != magic_number and counter > 0:
  counter-= 1
  print("You lose!")
  print("%s guesses remain." % (counter))
  print("")
  if counter == 0:
    break
  else:
    guess = int(input("Guess a number between 1 and 10:"))
else:
  print("You win!")
