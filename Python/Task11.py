#Create a program that prints numbers between 1 and 100 that are divisible by either 3 or 5 but not bot
values =[]
for num  in range(1,100):
    if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0):
        values.append(num)
print(values)
