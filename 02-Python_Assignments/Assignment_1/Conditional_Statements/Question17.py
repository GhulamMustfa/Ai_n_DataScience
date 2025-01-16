integer = int(input("Enter an Integer : "))

if integer % 3 == 0 and integer % 2 == 0:
    print("Its Divisible by both 2 and 3. ")
elif integer % 2 == 0:
    print("Its Divisible by 2. ")
elif integer % 3 == 0:
    print("Its Divisible by 3. ")
else:
    print("Its not divisible. ")
