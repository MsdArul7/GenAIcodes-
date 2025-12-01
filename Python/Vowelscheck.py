#Write a Python script to count how many vowels are present in a given string without using built-in count functions
count = 0
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)



        

        

    