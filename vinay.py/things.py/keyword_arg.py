# keyword arguments = am argumrnt preceeded by an indentifier
#                       helps with readability
#                       order of the arguments doesn't matter


#def hello(greeting, title,first, last):
#    print(f"{greeting} {title} {first} {last}")

#hello(greeting="Hello" , last="Smith" , first="John" , title="Mr.")


#for x in range(1,11):
#    print(x, end=" ") #here the argument end is a keyword argument for the print function


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1,area=234,first=567,last=890)

print(phone_num)
