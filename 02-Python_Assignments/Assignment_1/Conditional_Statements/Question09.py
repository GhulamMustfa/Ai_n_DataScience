
side1 = int(input("Enter first side of a triangle : "))
side2 = int(input("Enter second side of a triangle : "))
side3 = int(input("Enter third side of a triangle : "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Its a valid triangle. ")
else:
    print("Its not a valid triangle. ")

