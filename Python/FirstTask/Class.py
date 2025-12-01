class MathOperations:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print("Addition:", self.a + self.b)
    def subtract(self):
        print("Subtraction:", self.a - self.b)
    def multiply(self):
        print("Multiplication:", self.a * self.b)
    def divide(self):
        print("Division:", self.a / self.b)
result = MathOperations(10, 5)
result.add()
result.subtract()
result.multiply()
result.divide()

