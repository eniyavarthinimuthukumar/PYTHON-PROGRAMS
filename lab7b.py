student_details = {}

# Get the name from the user
name = input("Enter the name: ")

# Get the age from the user and check if it's positive
age = int(input("Enter the age: "))
if age < 0:
    print("Age should be positive. Skipping details...")
else:
    # Get the marks for 6 subjects from the user
    marks = []
    for i in range(6):
        subject_marks = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(subject_marks)

    # Add the details to the dictionary
    student_details["Name"] = name
    student_details["Age"] = age
    student_details["Marks"] = marks

# Print the generated dictionary
print("Student Details:", student_details)
