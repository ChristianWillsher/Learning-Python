# Type in the code for the guessing game here...
# Unlimited / 10 / 50 
import random

def generateNumber():
  print("generating a random number......")
  return random.randint(1,100)
  
number = generateNumber()
count = 0 
found = False

while not found:
  guess = int(input("Next guess:  "))
  count = count + 1 
  
  if guess < number:
    print("Too low!")
    
  if guess > number:
    print("Too high!")
    
  if guess == number:
    found = True 
    
print("You got it in", count, "guesses!")