# format specifiers = {:flags} format a value based on what flags are inserted
#.(number)f = round to a number of decimal places
#:(number)  = pad to a number of characters
#:03        = allocate and zero pad that many spaces 
#:<         = left align
#:>         = right align
#:^         = center align
#:+         = always show the sign of a number
#:=         = plsce sign to the leftmost position
#:          = space before positive numbers 
# :,        = commma seperator (thousands separator)




price1 = 123456.789
price2 = 987654.321
price3 = 456789.012

#print(f"price 1 is ${price1:.3f}")
#print(f"price 2 is ${price2:.3f}")
#print(f"price 3 is ${price3:.3f}")




#print(f"price 1 is ${price1:020}") # if you preceed the number with 0 it will zero pad the number
#print(f"price 2 is ${price2:>30}")  # left align




#print(f"price 1 is ${price1:+}") # tells sign 
#print(f"price 2 is ${price2:+}")
#print(f"price 3 is ${price3:+}")



print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")