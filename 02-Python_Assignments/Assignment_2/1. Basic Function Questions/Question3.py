def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is: {fact(num)}")
