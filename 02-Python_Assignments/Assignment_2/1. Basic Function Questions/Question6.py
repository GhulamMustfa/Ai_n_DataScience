def count(string):
    vowels = "aeiouAEIOU"
    count = 0
    for i in string:
        if i in vowels:
            count += 1

string = input("Enter a string: ")

print(f"The vowels in the string are: {count(string)}")
