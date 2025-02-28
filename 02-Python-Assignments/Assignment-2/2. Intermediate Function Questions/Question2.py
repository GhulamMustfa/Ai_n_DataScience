def find_nth_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return find_nth_fibonacci(n-1) + find_nth_fibonacci(n-2)
    
n = int(input("Enter the value of n: "))

print(find_nth_fibonacci(n))
