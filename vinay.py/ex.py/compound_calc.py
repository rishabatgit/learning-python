principle = 0 
rate = 0 
time = 0

while True :
    principle = float(input("Enter the principal amount (greater than 0): "))   
    if principle<= 0 :
        print("principal cant be less than zero !")
    else:
        break

while True : 
    rate = float(input("Enter the rate amount (greater than 0): "))   
    if rate<= 0 :
        print(" rate cant be less than zero ! ")
    else:
        break   


while True:
    time = int(input("Enter the time amount (greater than 0): "))   
    if time<= 0 :
        print("time cant be less than zero !")
    else:
        break



total = principle * pow((1 + rate /100),time)
print(f"Balance after {time} years is: ${total:.2f}")