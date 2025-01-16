num = int(input("Enter the number : "))
r_num = int(str(abs(num))[::-1])
if num < 0:
    r_num = -r_num
print(r_num)
