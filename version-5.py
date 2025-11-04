import random as rd

magic_number = rd.randint(1, 100)
# print(magic_number)

guess = int(input("Guess a number between 1 and 100:"))
counter = 10
 
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
else:
  print("You win!")
