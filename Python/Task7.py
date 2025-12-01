#Write a Python program that reads 5 names from the user and stores only the names that start with a vowel into a new listdefa = 
name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")
name3 = input("Enter name 3: ")
name4 = input("Enter name 4: ")
name5 = input("Enter name 5: ")
vowel_names = []
vowels = "aeiouAEIOU"
if name1[0] in vowels:
    vowel_names.append(name1)
if name2[0] in vowels:
    vowel_names.append(name2)
if name3[0] in vowels:
    vowel_names.append(name3)
if name4[0] in vowels:
    vowel_names.append(name4)
if name5[0] in vowels:
    vowel_names.append(name5)
print("Names starting with a vowel:", vowel_names)