# Lambda sorted function to add two numbers
students = [
    ("John", 25),
    ("Emily", 30),
    ("Adam", 22)
]
students = list(filter(lambda x: x[1] > 25, students))
print(students)



