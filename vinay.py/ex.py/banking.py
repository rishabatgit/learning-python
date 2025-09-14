def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def deposit():
    amount = float(input("Enter amount to deposit: "))

    if amount<0:
        print("Invalid amount. Please enter a positive value.")
        return 0
    else:
        return amount
    


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("Invalid amount. Please enter a positive value.")
        return 0
    else:
        return amount

def main():
    balance = 0 
    is_running = True

    while is_running:

        print()
        print("**********************")
        print("Banking program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice. Please try again.")


    print("Thank you for using the banking program.")

if __name__ == "__main__":
    main()