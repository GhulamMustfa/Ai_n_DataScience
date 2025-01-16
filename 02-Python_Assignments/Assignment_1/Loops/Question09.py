a = 0
b = 1
print(a)
print(b)
for num in range(1,11):
    c = a + b
    a=b
    print(c)
    b=c
