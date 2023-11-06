# Function to calculate the average of course marks
def calculate_average(course_marks):
    total_marks = sum(course_marks)
    average = total_marks / len(course_marks)
    return average

# Input the number of courses
num_courses = int(input("Enter the number of courses: "))

# Initialize a list to store course marks
course_marks = []

# Input marks for each course
for i in range(num_courses):
    mark = float(input(f"Enter marks for course {i+1}: "))
    course_marks.append(mark)

# Calculate the average of course marks
average = calculate_average(course_marks)

# Assume the total marks for all courses is 500
total_marks = 500

# Calculate the percentage
percentage = (sum(course_marks) / total_marks) * 100

# Display the results
print(f"Average marks for all courses: {average}")
print(f"Percentage obtained: {percentage}%")
