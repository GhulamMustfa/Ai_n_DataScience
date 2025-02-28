# Print the sum of even and odd numbers separately up to a given number.

num = int(input("Enter the number : "))

print("Even numbers : ")
for e in range(2,num+1,2):
    print(e)

print("Odd numbers : ")
for o in range(1,num+1,2):
    print(o)
