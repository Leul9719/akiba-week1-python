
USD_Amount = int(input ("How much do u want to exchange: "))
Rate = 150
ETB_Amount = USD_Amount*Rate
print("="*40)
print("        CURRENCY EXCHANGE")
print("="*40)
print(f"USD Amount: {USD_Amount}")
print(f"Exchange rate: 1 USD = {Rate}")
print(f"ETB Amount: {ETB_Amount}")
print("="*40)

print("Choose your exchange rate: ")
Rate1 = int(input("What is the exchange rate: "))
ETB_Amount2 = USD_Amount*Rate1
print("="*40)
print("        CURRENCY EXCHANGE")
print("="*40)
print(f"USD Amount: {USD_Amount}")
print(f"Exchange rate: 1 USD = {Rate1}")
print(f"ETB Amount: {ETB_Amount2}")
print("="*40)
