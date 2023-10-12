# Define the cost of a single USB stick and the girl's budget
usb_stick_cost = 6  # in pounds
budget = 50  # in pounds

num_usb_sticks = budget // usb_stick_cost  

# Calculate how much money she will have left
money_left = budget % usb_stick_cost  

print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have £{money_left} left.")
