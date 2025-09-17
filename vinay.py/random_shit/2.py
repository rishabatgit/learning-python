import random 

lowest = 1
highest = 100
Answer = random.randint(lowest,highest)
guesses = 0 
is_running = True


while is_running:
    guess= input("Enter a no between 1 and 100 : ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1 
        if guesses>10:
            print("You have exceeded the number of guesses")
            print(f"The correct answer was {Answer}")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again=="y":
                Answer = random.randint(lowest,highest)
                guesses = 0
            else:
                is_running = False

        elif guess <lowest or guess> highest:
            print("Out of range")
            print(f"Select a no between {lowest} and {highest} ")

        elif guess < Answer:
            print("TOO low try again!")

        elif guess> Answer:
            print("TOO high try again!")

        else:
            print(f"CORRECT! The answeer was {Answer}")
            print(f"No of guesses : {guesses}")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again=="y":
                Answer = random.randint(lowest,highest)
                guesses = 0
            else:
                is_running = False
    else:
        print("Invalid guess")
        print(f"Select a no between {lowest} and {highest} ")   
     