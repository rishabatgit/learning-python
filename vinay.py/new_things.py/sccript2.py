from script1 import *

def favorite_drink(drink):
    print(f"your favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("Goodbye")

if __name__ == "__main__":
    main()