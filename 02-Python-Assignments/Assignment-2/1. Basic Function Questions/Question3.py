def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist of a negative numbers")
else:
    print(f"The factorial of {num} is: {fact(num)}")
