# add three number to find and sum average
a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")
sum = int(a) + int(b) + int(c)
average = sum / 3
print("Sum:", sum)
print("Average:", average)

n = int(input("Enter the number of terms in Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

