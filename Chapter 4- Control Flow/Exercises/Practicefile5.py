# Get the month as input
month = int(input("Enter the month (1-12): "))

if 1 <= month <= 12:
    if 3 <= month <= 5:
        season = "Spring"
    elif 6 <= month <= 8:
        season = "Summer"
    elif 9 <= month <= 11:
        season = "Autumn (Fall)"
    else:
        season = "Winter"
    print(f"The season for month {month} is {season}")
else:
    print("Invalid input. Please enter a valid month (1-12).")
