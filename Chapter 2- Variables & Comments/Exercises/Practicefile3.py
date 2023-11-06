# Input 5 values from the user
input_values = []
for i in range(5):
    value = input(f"Enter value {i+1}: ")
    input_values.append(value)

# Typecast the values to string, int, and float
str_values = list(map(str, input_values))
int_values = list(map(int, input_values))
float_values = list(map(float, input_values))

print("As Strings:", str_values)
print("As Integers:", int_values)
print("As Floats:", float_values)
