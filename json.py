# Step 1: Create a Python dictionary with student details and write to `students.json`
import json

# Create a Python dictionary
students = [
    {"name": "Alice", "age": 20, "marks": 80},
    {"name": "Bob", "age": 21, "marks": 60},
    {"name": "Charlie", "age": 22, "marks": 75}
]

# Write to JSON file
with open('students.json', 'w') as file:
    json.dump(students, file, indent=4)
# Step 2: Read data back and print students with marks > 70
with open('students.json', 'r') as file:
    students_data = json.load(file)

# Print students with marks > 70
students_marks_gt_70 = [student for student in students_data if student['marks'] > 70]
print("Students with marks > 70:")
print(students_marks_gt_70)
# Step 3: Convert JSON file content to a JSON string and print
with open('students.json', 'r') as file:
    json_string = file.read()

print("\nJSON string:")
print(json_string)