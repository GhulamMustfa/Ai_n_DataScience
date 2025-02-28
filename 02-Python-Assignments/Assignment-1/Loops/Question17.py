# Write a program that continues to ask for a number until the correct number is guessed.

num = int(input("Enter the number : "))

while num != 5:
    print("Wrong ")
    num = int(input("Try Again : "))

print("Well guessed, 5")
