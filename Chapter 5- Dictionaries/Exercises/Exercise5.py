# Create a list of dictionaries representing different pets
pets = [
    {"kind": "Dog", "owner": "Anum"},
    {"kind": "Cat", "owner": "Maryum"},
    {"kind": "Fish", "owner": "Basim"},
    {"kind": "Bird", "owner": "Hammad"},
]

# Loop through the list and print information about each pet
for pet in pets:
    kind = pet["kind"]
    owner = pet["owner"]
    print(f"This is a {kind} and the owner's name is {owner}.")
