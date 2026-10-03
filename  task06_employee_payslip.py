
employee_name = input("Enter your name: ")
basic_salary = int(input("What is you basic salary: "))
transport_allowance = int(input("Allowance for transport: "))
food_allowance = int(input("Allowance for food: "))

Gross_salary = basic_salary + transport_allowance + food_allowance

print("="  * 40)
print("             EMPLOYEE PAYSLIP")
print("=" * 40)
print("")
print(f"Employee: {employee_name}")
print(f"Basic Salary:      {basic_salary}ETB")
print(f"Transport Allowance:     {transport_allowance}ETB")
print(f"Food Allowance:      {food_allowance}ETB")

print("-" * 30)
print(f"Gross Salary:        {Gross_salary}ETB")
