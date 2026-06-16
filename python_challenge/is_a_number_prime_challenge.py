def is_prime(n):
    divisor = 1
    count = 0
    while divisor <= n:
        if n % divisor == 0:
            count += 1
        divisor += 1
        
    if count == 2:
        print("True")
    else: 
        print("False")

is_prime(9)