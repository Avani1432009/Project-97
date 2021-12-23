#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lenovo
#
# Created:     20-12-2021
# Copyright:   (c) lenovo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
print("number guessing game")

number = random.randint(1,9)
chances = 0
print('guess a number(between 1 and 9):')

while chances < 5:
    guess = int(input("Enter your guess"))

if guess == number:
    print("Congratulation You Won!!!")
    break

elif guess < number:
    print("Your guess was too low: guess a number higher than", guess)

else:
    print("Your guess was too high: guess a number lower than", guess)
    
chances += 1 

if not chances < 5:
    print("You lose!!! the number is: ", number)
