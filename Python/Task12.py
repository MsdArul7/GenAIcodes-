#Write a Python program that asks for apassword and grants access only if the password matches and the user has not exceeded 3 failed attempts (use while loop and logical operators).
correct_password = "secure123"
attempts = 0
while attempts < 3:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        attempts += 1
        print(f"Incorrect password. You have {3 - attempts} attempts left.")