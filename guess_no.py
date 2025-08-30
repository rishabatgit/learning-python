import random

lowewst = 1
highest = 100 
answer = random.randint(lowewst,highest)
guesses = 0
is_running = True


print("-----------------------------------------------")
print("Python number guessing game ")
print(f"select a number between {lowewst} and {highest} ")

while is_running:

    guess = input("Enter your guess:  ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1 

        if guess < lowewst or guess > highest:
            print("That number is out of range ")
            print(f"select a number between {lowewst} and {highest} ")

        elif guess < answer:
            print("Too low try again ")
        elif guess > answer :
            print("Too high try again ")
        else:
            print(f"CORRECT ! The answer was {answer}")
            print(f"no of guesses : {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f" please select a number between {lowewst} and {highest} ")














