questions = (" What's your favorite way to spend a weekend?: ",
             " What's a book that has significantly impacted you and why?: ",
             " What's a skill you'd love to learn and why?: ",
             " What's a cause or issue you're passionate about?: ",
             " What's a piece of advice you would give to your younger self?: ")


options = (("A. dance","B. movie ","C. art ","D. study "),
           ("A. theory","B.english ","C. maths ","D. science "),
           ("A. coding ","B. art ","C. sing ","D. hakla "),
           ("A. cancer ","B. space","C. trafficking ","D. illegal "),
           ("A. dance ","B. gf ","C. study ","D. eat "))


answers = ("C","D","A","B","C")
guesses = []
score  = 0 
question_num = 0 



for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=( input("enter(A,B,C,D):")).upper
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1 
        print("CORRECT")
    else:
        print("INCORRECT!!!")  
        print(f"{answers[question_num]} is true ")
    question_num += 1 

print("-------------------------------------")
print("             RESULTS                 ")
print("-------------------------------------")

print("answers: ", end = "")
for answer in answers:
    print(answer, end = "")
print()



print("guesses: ", end = "")
for guess in guesses:
    print(answer,end="")
print()



score = int(score/len(questions)  *100)
print(f"your score is :{score}%")













