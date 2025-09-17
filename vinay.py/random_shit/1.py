
import random


def spin_row():
    symbold = ["🍒", "🍋", "🍈", "🔔", "⭐"]
    return [random.choice(symbold) for symbol in range(3)]

def print_row(row):
    print(" |".join(row))


def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet*3
        elif row[0]=="🍋":
            return bet*4
        elif row[0]=="🍈":
            return bet*5
        elif row[0]=="🔔":
            return bet*10
        elif row[0]=="⭐":
            return bet*20
    return 0 

def main():
    balance = 100
    print("────────────────────────")
    print("Welcome to Slot Machine! ")
    print("Symbols: 🍒 🍋 🍈 🔔 ⭐ ")
    print("────────────────────────")

    while balance >0:
        print(f"Current balnce is {balance}")

        bet = input("place your bet amount:  $")
        if not bet.isdigit():
            print("Invalid input please enter a numeric value")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insuffficient balance!")
            continue
        if bet <=0:
            print("Bet should be greater than zero")
            continue 

        balance -=bet

        row = spin_row()
        print("Spinning. . . . \n")

        print_row(row) 

        payout = get_payout(row,bet)
        
        if payout >0:
            print(f"You won ${payout}!")
        else:
            print("Better luck next time!")


        balance +=payout

        play_again = input("Do you want to play again? (Y/n): ").lower()
        if play_again != "y":
            break 

    print(f"You are leaving with ${balance}. Thanks for playing!")        



if __name__ == "__main__":
    main()
