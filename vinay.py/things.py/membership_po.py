# membership operarators = used to test weather a value or variable is found in a sequence (string, list, tuple, set, dictionary)
#                           (string,tuple,list,set.dictionary)
#                           1. in
#                           2. not in
# it is a booolean operator (true or false) it returns true if the value is found in the sequence and false if it is not found in the sequence


#word = "APPLE"

#letter = input("guess a letter: ").upper()

#if letter in word:
#    print(f"yes {letter} is in the word")

#else:
#    print(f"no {letter} is not in the word")






#students = {"spongebob", "patrick", "sandy", "squidward"}

#student = input("Enter the name of a student: ").lower()

#if student not in students:
#    print(f"{student} is not in the class")
#else:
#    print(f"{student} is in the class")







#grades = {"sandy":"A", "spongebob":"B", "patrick":"C", "squidward":"D"}

#student = input("Enter the name of a student: ").lower()

#if student in grades:
#    print(f"{student}'s grade is {grades[student]}")
#else:
#    print(f"{student} is not in the class")





email = input("Enter your email: ")
if "@" in email and ".com" in email:
    print("valid email")
else:
    print("invalid email")


