# Create a list of places to visit
places_to_visit = ["Paris", "Tokyo", "Berlin", "New York", "Denver"]

# Print the list in its original order
print("Original list:")
print(places_to_visit)

# Print the list in alphabetical order without modifying the actual list
print("\nSorted list (alphabetical):")
print(sorted(places_to_visit))

# Check that the original list is still in its original order
print("\nOriginal list:")
print(places_to_visit)

# Print the list in reverse alphabetical order without changing the original list
print("\nSorted list (reverse alphabetical):")
print(sorted(places_to_visit, reverse=True))

# Check that the original list is still in its original order
print("\nOriginal list:")
print(places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()
print("\nReversed list:")
print(places_to_visit)

# Change the order of the list again using reverse()
places_to_visit.reverse()
print("\nReversed back to the original order:")
print(places_to_visit)

# Change the order of the list using sort() to alphabetical order
places_to_visit.sort()
print("\nSorted list (alphabetical):")
print(places_to_visit)

# Change the order of the list using sort() to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("\nSorted list (reverse alphabetical):")
print(places_to_visit)
