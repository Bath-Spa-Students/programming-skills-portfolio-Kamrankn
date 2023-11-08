largest = None
num = 1 

# Use a while loop to find the largest number
while num != 0:
    num = int(input("Enter a number (0 to exit): "))
    
    if num == 0:
        break  # Exit the loop when '0' is entered
    
    if largest is None or num > largest:
        largest = num

if largest is not None:
    print("The largest number entered was:", largest)
else:
    print("No valid numbers entered.")
