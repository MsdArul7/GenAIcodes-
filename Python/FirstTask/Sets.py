#Write a code using sets get a info of for creating a student database
student = set()
student_info = input("Enter the number of students to add to the database: ")
while True:
    names = input("Enter student name (or type 'done' to finish): ")
    age = input("Enter student age: ")
    emp_id = input("Enter student ID: ")
    student.add((names, age, emp_id))
    print("Student added to the database.")
    cont = input("Do you want to add another student? (yes/no): ")
    if cont.lower() != 'yes':
        break
print("Student Database:")
for info in student:    
    print(f"Name: {info[0]}, Age: {info[1]}, ID: {info[2]}")
print("Total number of students in the database:", len(student))