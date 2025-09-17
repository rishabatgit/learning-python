word = input("Enter a word or number you want to check!: ").lower()
if word.isdigit():
    if word == word[::-1]:
        print(f"{word} is a palindrome number")
    else:
        print(f"{word} is not a palindrome number")
else:
    if word == word[::-1]:
        print(f"{word} is a palindrome word")
    else:
        print(f"{word} is not a palindrome word")