#Using logical operators, write a program that accepts a user’s age and salary and determines if they are eligible for a loan (age ≥ 21 and salary ≥ ₹25,000)
status=[]
age = int(input("Enter the age "))
salary = float(input("Enter The salary "))
if age >=21 and salary >=25000:
    print(f"{age }You are eligible")
else:
    print(f"{salary}you are not eligible")
    status.append((age,salary))
print("Ineligible applicants:", status)

    
