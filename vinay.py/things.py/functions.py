#function =  a block of reusable code 
#               place () after the fuction name to invoice it 

#def happy_birthday(name,age):
#    print(f"Happy birthday{name}")
#    print(f"you are {age} years old ")
#    print("Happy birthday to you ")
#    print()


#happy_birthday("steve",20)
#happy_birthday("chicken_jockey",2)



# return = statemeny used to end a function 
#           and send the result back to the caller



#def add(x,y):
#    z = x+y
#    return z 

#def subtract(x,y):
#    z = x-y
#    return z 

#def multiply(x,y):
#    z = x*y
#    return z 

#def divide(x,y):
#    z = x/y
#    return z


#print(subtract(4,5))
#print(multiply(5,7))
#print(divide(4,2))



def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("vinay","singh")
print(full_name)