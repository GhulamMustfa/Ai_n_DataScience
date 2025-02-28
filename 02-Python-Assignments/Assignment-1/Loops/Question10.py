num = int(input("Enter the integer : "))

a = 0
while num > 0:
    num = num // 10
    a += 1
print(a)