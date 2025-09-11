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






fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits = [ fruit.upper() for fruit in fruits]
print(fruits)