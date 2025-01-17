# Create a program that simulates a countdown timer starting from a given number down to zero.
import time

num = int(input("Enter the time : "))

while num >= 1:
    print(num)
    num = num - 1
    time.sleep(0.5)
