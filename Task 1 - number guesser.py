#random number guesser
import random

top_of_range=input("Type a number: ")


if top_of_range.isdigit():
  top_of_range = int(top_of_range)
   
  if top_of_range <=0:
    print('Type a number greater than 0')
    quit()
else:
  print('Type a number next time')
  quit()

random_number = random.randrange(0, top_of_range)
guesses = 0

while True:
  guesses +=1
  user_guess = input("make a guess: ")
  if user_guess.isdigit():
      user_guess = int(user_guess)
  else:
    print("Type anumber next time")
    continue

  if user_guess == random_number:
    print("you got it!!!!")
    break
  else:
      if user_guess> random_number:
            print('you were above the number')
      else:
         print('you were below the number')

print("you got it in " + str(guesses) + " guesses")
