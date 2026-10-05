
Name = input("What is your name: ")
Weight = int(input("How much do you weigh in kilograms: "))
Height = float(input("How tall are you in meters: "))

BMI = Weight/(Height*Height)
print("="*40)
print(".        BMI REPORT")
print("="*40)
print(f"Name: {Name}")
print(f"Weight: {Weight}kg")
print(f"Height: {Height}m")
print(f"BMI: {BMI}")
print("="*40)