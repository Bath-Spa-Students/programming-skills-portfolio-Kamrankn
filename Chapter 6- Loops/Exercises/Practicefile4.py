# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize a variable to store the first even number
first_even = 24
# Use a for loop to find the first even number
for number in numbers:
    if number % 2 == 0:
        first_even = number
        break  # Exit the loop when the first even number is found

if first_even is not None:
    print("The first even number is:", first_even)
else:
    print("No even number found in the list.")
