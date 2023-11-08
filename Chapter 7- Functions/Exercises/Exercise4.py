def make_shirt(size="Large", message="I love Python"):
    print(f"Creating a {size}-sized shirt with the message: {message}")

# Call the function with default values
make_shirt()  

# Call the function to create a medium shirt with the default message
make_shirt("Medium")

# Call the function to create a custom-sized shirt with a different message
make_shirt("Small", "Beleive in Yourself!")
