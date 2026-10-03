
customer_name = input("Enter your name: ")
product_name = input("What product would u like to purchase: ")
price = int(input(": "))
quantity = int(input("How many/much do you want: "))

total_price = price*quantity

print("=" * 40)
print("              RECEIPT")
print("=" * 40)

print("Product        Price       Qty")
print("-" * 20)
print(f"{product_name}    {price}   {quantity}")
print("")
print("")
print(f"Totat:    {total_price}")

print("Thank you for shopping!")
print("=" * 40)
