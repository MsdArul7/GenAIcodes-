#Using nested if-else, write a program that classifies a triangle as equilateral, isosceles, or scalene based on user input sides.
side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Invalid side lengths. All sides must be positive numbers.")
else:
    if side1 == side2:
        if side2 == side3:
            print("The triangle is equilateral.")
        else:
            print("The triangle is isosceles.")
    else:
        if side1 == side3 or side2 == side3:
            print("The triangle is isosceles.")
        else:
            print("The triangle is scalene.")