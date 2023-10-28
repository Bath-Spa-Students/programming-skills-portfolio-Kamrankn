# Define the initial programming glossary
programming_glossary = {
    "variable": "A storage location in a program that holds data.",
    "function": "A reusable block of code that performs a specific task.",
    "algorithm": "A step-by-step procedure for solving a problem or accomplishing a task.",
    "loop": "A control structure that repeats a sequence of instructions.",
    "conditional statement": "A statement that allows the program to make decisions based on a condition."
}

# Print the original glossary
for word, meaning in programming_glossary.items():
    print(word + ": " + meaning + "\n")

# Add five more Python terms to the glossary
programming_glossary["list"] = "A collection of ordered and changeable elements."
programming_glossary["dictionary"] = "A collection of key-value pairs."
programming_glossary["module"] = "A file containing Python code that can be imported and used in other programs."
programming_glossary["exception"] = "An event that occurs during program execution that disrupts the normal flow."
programming_glossary["method"] = "A function associated with an object or a class."

# Print the updated glossary
print("\nUpdated Glossary:")
for word, meaning in programming_glossary.items():
    print(word + ": " + meaning + "\n")
