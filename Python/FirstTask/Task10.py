#Write a Python script that reads a list of marks and prints “Pass” if all marks are above 40, otherwise “Fail”, using logical AND.
def check_pass_fail(marks):
    for mark in marks:
        if mark <= 40:
            return "Fail"
    return "Pass"
marks = []
num_marks = int(input("Enter the number of marks: "))
for i in range(num_marks):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)
result = check_pass_fail(marks)
print(result)
