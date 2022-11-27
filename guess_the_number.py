#program that asks user to guess a number 6 times.

import random
secret_number=random.randint(1,50)  #secret number is created
print("Enter a number between 1 to 50. You wil get 6 attempts to guess the correct number")

for i in range(1,7): #loops 6 times
    guess_number=int(input("Enter your Guess: "))  #asks user for input
    if guess_number<secret_number:
        print("Your guess is low. Enter a higher number")
    elif guess_number>secret_number:
        print("Your guess is high. Enter a smaller number.")
    else:
        break

if guess_number==secret_number:
    print('Bravo..! Your guess was right in'+str(i)+'th attempt.')
else:
    print('You are put of guesses. Correct number is '+str(secret_number)+'.')
