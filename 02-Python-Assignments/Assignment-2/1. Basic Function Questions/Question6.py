def counting(string):
    vowels = "aeiouAEIOU"
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    print(f"The vowels in the string are: {count}")

string = input("Enter a string: ")

counting(string)
