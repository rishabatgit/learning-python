# list comprehension = a concise way to create lists in python 
#                  compact and easier to read than traditiomal loops
#                    [expression for value in iterable if condition]


#doubles = []
#for x in range(1,11):
#    doubles.append(x*2)
#print(doubles)
#                          OR

#doubles = [x*2 for x in range(1,11)]
#squares = [z*z for z in range(1,11)]
#print(doubles)
#print(squares)






#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#fruits = [ fruit.upper() for fruit in fruits]
#print(fruits)




#numbers = [1,2,3,4,5,6,7,-8,9,10]
#psitive_num =[num for num in numbers if num>=0]
#print(psitive_num)








grades = [65, 90, 75, 82, 55, 98, 100, 45, 73]
passe_students = [grade for grade in grades if grade>=60]
fail_stdents = [grade for grade in grades if grade<60]
print(f"pass students: {passe_students}")
print(f"fail students: {fail_stdents}")
