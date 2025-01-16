for num in range(2,50):
    for prime in range(2,num):
        if num % prime == 0:
            break
    else:
        print(num)