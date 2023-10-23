# Create a list of transportation modes
transportation_modes = ["motorcycle", "car", "bicycle", "train", "airplane"]

# Generate statements about each mode of transportation
for mode in transportation_modes:
    if mode == "motorcycle":
        print(f"I would like to own a {mode}.")
    elif mode == "car":
        print(f"I own a {mode}.")
    elif mode == "bicycle":
        print(f"I enjoy riding my {mode}.")
    elif mode == "train":
        print(f"I've traveled on a {mode} before.")
    elif mode == "airplane":
        print(f"I have flown in an {mode}.")
    else:
        print(f"I'm not sure what to say about {mode}.")
