#Using a while loop, reverse the digits of a given integer (e.g., 12345 → 54321)
def reverse_integer(num):
    reversed_number = 0
    while num > 0:
        digit = num % 10
        reversed_number = reversed_number * 10 + digit
        num = num // 10
    return reversed_number

num = int(input("Enter an integer: "))
print("The reversed number is", reverse_integer(num))



