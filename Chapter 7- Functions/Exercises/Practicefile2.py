def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: factorial(n) = n * factorial(n-1)
        return n * factorial(n - 1)

# Example usage:
number = 7
result = factorial(number)
print(f"The factorial of {number} is:", result)
