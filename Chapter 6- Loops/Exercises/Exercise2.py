while True:
    age = input("Please enter your age (or 'quit' to exit): ")

    if age.lower() == 'quit':
        break

    age = int(age)  # Convert the input to an integer

    if age < 3:
        print("Your ticket is free.")
    elif age >= 3 and age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
