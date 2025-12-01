class student_info:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
result = student_info("Alice", 20, 95)
result.display_info()
#use parent class to inherit the properties
class UGstudent_details(student_info):
    def __init__(self,name,age,marks,department):
        self.department = department
        self.name = name
        self.age = age
        self.marks = marks
    def display_ug_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}, Department: {self.department}")
result = UGstudent_details("Bob",21,88,"Computer Science")
result.display_ug_info()

