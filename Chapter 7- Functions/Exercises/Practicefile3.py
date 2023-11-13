def is_prime(number):
    # Prime numbers are greater than 1
    if number > 1:
        # Check for factors from 2 to the square root of the number
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False  
        return True  
    else:
        return False 

# Numbers less than or equal to 1 are not prime
num = 39 
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
