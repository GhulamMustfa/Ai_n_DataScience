def palindrome(s):
    space = s.replace(" ", "")
    if space == space[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

s = input("Enter a string: ")
palindrome(s)
