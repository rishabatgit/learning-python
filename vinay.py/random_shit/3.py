# shopping cart 

Items = []
Price = []
Total = 0

while True:
    item = input("Enter an item(q to quit)")
    if item.lower()=="q":
        break
    else:
        price = float(input("Enter the price of the Item you want to buy"))
        Items.append(item)
        Price.append(price)
        Total+=price

print("\nYOUR CART: ")
for item,price in zip(Items,Price):
    print(f"- {item}: ${price}")
print(f"Total: ${Total}")

