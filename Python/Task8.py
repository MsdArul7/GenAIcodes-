#Write a while loop program that keeps asking the user to enter a positive number and stops only when the user enters a 
positive_number=[]
while True:
    number = int(input("Enter a positive number (or a negative number to stop): "))
    if number < 0:
        print("Negative number entered. Stopping the program.")
        break
    positive_number.append(number)
print("positive numbers entered:", positive_number)
