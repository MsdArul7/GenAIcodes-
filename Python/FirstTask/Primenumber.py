# Write a Python program to print all prime numbers between 10 and 100 using a for loop and if conditions

for a in range(10, 101):
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                print(a, "is not a prime number")
                break
        else:
            print(a, "is a prime number")
