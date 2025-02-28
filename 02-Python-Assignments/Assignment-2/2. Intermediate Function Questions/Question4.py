def sum_even(numbers):
    sum = 0
    for s in numbers:
        if s % 2 == 0:
            sum += s
    print(sum)

numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
sum_even(numbers)
