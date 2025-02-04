def gcd_find(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
        
    for i in range(1, small + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcd = i
    return hcd

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The GCD of", num1, "and", num2, "is", gcd_find(num1, num2))
