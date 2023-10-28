programming_glossary = {
    "variable": "A storage location in a program that holds data.",
    "function": "A reusable block of code that performs a specific task.",
    "algorithm": "A step-by-step procedure for solving a problem or accomplishing a task.",
    "loop": "A control structure that repeats a sequence of instructions.",
    "conditional statement": "A statement that allows the program to make decisions based on a condition."
}

# Printing each word and its meaning with a blank line between each pair
for word, meaning in programming_glossary.items():
    print(word + ": " + meaning + "\n")
