student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "rudra":100
}

student_name = input("Enter the student's name: ")

if student_name in student_marks:
    print(f"{student_name}'s marks are: {student_marks[student_name]}")
else:
    print(f"Sorry, no marks found for student named '{student_name}'.")
