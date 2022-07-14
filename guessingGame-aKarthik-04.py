'''Program:Guessing Game  
         Author:Arun Karthik
         Description:This program will make the user to guess a number in fewest number of gusses.  .
         Revisions:
         00-Importing the Math and Random Module 
         01-User will input the secret number 
         02-Calculate the maximum number of guesses
         03-Assigning the secret number
         04-Printing the result if the guess is correct 
        '''

# Importing the math and Random module 
import math
import random

#Annoucement 
print("Guess the secret Number ")

# User will input the secret number 
secret = int(input("Enter the secret number "))

nguess = int(math.log2(secret)+1)

randomNumber= random.randint(1,secret)

for i in range(1,nguess + 1):
    number = int(input("Enter your guess: "))

    if number == randomNumber:
        print('Correct.Well done!\n')
        break
    
# secret number is greater than guessed number 
    if number >randomNumber:
        print("The secret number is less than",number)
        nguess -=1
        print("You have ",nguess,"guesses available")
        
# secret number is less than guessed number

    if number< randomNumber:
        print("The secret number is greater than",number)
        nguess -=1
        print("You have",nguess,"guesses available")

    if nguess == 0 and number!=randomNumber:
        
# Print the result
        print("Sorry.No more guess are allowed.")
        print("The secret number was",nguess,".")
