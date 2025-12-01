#Write a p(rogram to collect all the students information and find who is score maximum using Tuples 
students = []
num_students = int(input("Enter the number of students: "))
while True: 
    name = input("Enter The name ")
    age = int(input("Enter The age "))
    marks = int(input("Enter the Marks "))
    students.append((name, age, marks))
    num_students -= 1
    if num_students == 0:
        break
    #convert list to tuple
students = tuple(students)
print("Students info")
#Finding the student with maximum score using lambda function
max_score_student = max(students, key=lambda x: x[2])
print(f"Top student is {max_score_student[0]} with marks {max_score_student[2]}")