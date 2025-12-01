# Write a program that continuously reads integers from the user and writes them into a file until the user types “STOP”; then print the total count of even and odd numbers written
even_count = 0
odd_count = 0  
with open("numbers.txt", "w") as file:
    while True:
        user_input = input("Enter an integer (or type 'STOP' to finish): ")
        if user_input.upper() == "STOP":
            break
        try:
            number = int(user_input)
            file.write(f"{number}\n")
            if number % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        except ValueError:
            print("Invalid input. Please enter an integer or 'STOP'.")
print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")