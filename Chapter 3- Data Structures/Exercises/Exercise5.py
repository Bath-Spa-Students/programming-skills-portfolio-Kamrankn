# Create a list of people to invite to dinner
guests = ["Taha", "Basim", "Umer"]

# Print the name of the guest who can't make it
guest_cant_make_it = "Umer"
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.")

# Replace the guest who can't make it with a new person
new_guest = "Rafay"
guests.remove(guest_cant_make_it)
guests.append(new_guest)

# Generate dinner invitations for each remaining guest
for guest in guests:
    invitation = f"Dear {guest},\n\nYou are invited to a dinner at my place on Sunday. Please join us for an evening of good food and great conversation.\n\nSincerely, Kamran"
    print(invitation)
