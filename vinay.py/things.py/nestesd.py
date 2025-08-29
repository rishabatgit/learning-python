# nested loop = A loop within another loop (oouter,inner)
#               outer loop:
#                      inner loop :




#for x in range(3):
#    for y in range(1,10):
#        print(y,end="")
#    print()




rows = int(input("Enter the number of rows : "))
columns = int(input("enter the no of columns: "))
symbol = input("enter a symbol to use :")



for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()





















