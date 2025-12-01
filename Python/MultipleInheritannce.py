class Student:
    school = "ItTechGenie Academy"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):                      # Instance Method
        print(f"Name: {self.name}, Marks: {self.marks}")

    @classmethod
    def school_info(cls):                # Class Method
        print(f"School Name: {cls.school}")

    @staticmethod
    def greet():                         # Static Method
        print("Welcome to ItTechGenie Python Course!")

Student.greet()
Student.school_info()
s1 = Student("Divya", 88)
s1.show()