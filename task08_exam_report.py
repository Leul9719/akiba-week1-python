
Student_name = input("What is your name: ")
Python_score = int(input("What is your python score: "))
English_score = int(input("What is your English score: "))
Maths_score = int(input("What is your Mathematics score: "))

Average = (Python_score + English_score + Maths_score)/3

print("="*40)
print("          STUDENT RESULT")
print("="*40)
print(f"Student: {Student_name}")
print(f"Python:      {Python_score}")
print(f"English:      {English_score}")
print(f"Mathematics:   {Maths_score}")
print("-"*20)
print(f"Average:  {Average}")
print("="*40)