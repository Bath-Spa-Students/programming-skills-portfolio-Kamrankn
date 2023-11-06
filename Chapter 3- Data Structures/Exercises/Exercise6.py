# Create a list of people to invite to dinner
guests = ["Taha", "Basim", "Umer"]

# Print a message stating that only two people can be invited
print("I can only invite two people for dinner.")

# Remove guests one at a time until only two names remain
while len(guests) > 2:
    guest = guests.pop()
    print(f"Sorry, {guest}, I can't invite you to dinner.")

# Print invitations for the two remaining guests
for guest in guests:
    invitation = f"Dear {guest},\n\nYou are invited to a dinner at my place on Sunday.\
 Please join us for an evening of good food and great conversation.\n\nSincerely, Kamran"
    print(invitation)

# Use del to remove the last two names
del guests[:]

# Print the list to confirm it's empty
print("Guest list is empty:", guests)
