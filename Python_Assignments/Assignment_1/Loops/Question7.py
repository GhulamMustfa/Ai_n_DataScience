num = int(input("Enter the number : "))

if num <= 0:
    print("Error, The cannot be smaller than 1")
else:
    f = 1
    a = 1
    while a <= num:
        f = f * a
        a += 1
    print(f)