# Create a code using list  to store names paraticipated in an event and print in list format.
names = []
num_names = int(input("Enter the number of participants: "))
for i in range(num_names):
    name = input(f"Enter the name of participant {i + 1}: ")
    names.append(name)
    print(f"Participant added: {name}")
print("\nList of participants:")
for name in names:
    print(name)

