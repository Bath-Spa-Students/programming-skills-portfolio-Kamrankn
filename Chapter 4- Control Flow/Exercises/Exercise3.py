alien_color = 'green'

if alien_color == 'green':
    print("Player earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")    #The alien_color is set to 'green', so the first condition is met, and it prints "Player earned 5 points."

alien_color = 'yellow'

if alien_color == 'green':
    print("Player earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")    #The alien_color is set to 'yellow', so the second condition is met, and it prints "Player earned 10 points."

alien_color = 'red'

if alien_color == 'green':
    print("Player earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")    # the alien_color is set to 'red', which does not match the conditions in the if and elif statements. Therefore, it falls to the else block and prints "Player earned 15 points."
