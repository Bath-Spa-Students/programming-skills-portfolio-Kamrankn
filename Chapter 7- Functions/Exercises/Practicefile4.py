import math

def calculate_circle_area(radius):
    # Area of a circle formula: A = π * r^2
    area = math.pi * radius**2
    return area

# 
radius = 8  
result = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is: {result:.2f}")
