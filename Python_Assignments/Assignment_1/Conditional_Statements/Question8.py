text = input("Enter the word : ")

l_text = text.replace(" ","").lower()

if l_text == l_text[::-1]:
    print(f"{text} a Palindrome")
else:
    print(f"{text} is not a Palindrome")
