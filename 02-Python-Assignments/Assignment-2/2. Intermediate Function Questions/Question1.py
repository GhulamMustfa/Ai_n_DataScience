def return_biggest_number():
    numbers = list(map(float, input("Enter the numbers separated by spaces: ").split()))
    return max(numbers)

print(return_biggest_number())
