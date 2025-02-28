# Create a program to calculate the sum of the digits of an inputted integer.

num = str(abs(int(input("Enter the integer : "))))

sum = 0
for digits in num:
    sum = sum + int(digits)
print(sum)
