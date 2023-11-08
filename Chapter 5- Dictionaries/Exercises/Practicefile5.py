# Create two sample dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"c": 4, "d": 5, "e": 6}

# Merge dict2 into dict1
dict1.update(dict2)

# The result will be stored in dict1
print("Merged Dictionary (using update()):", dict1)
