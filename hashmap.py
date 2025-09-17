
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David"
}

# Print all students
print("Student List (RollNo -> Name):")
for roll, name in students.items():
    print(roll, "->", name)

print("\nStudent with Roll No 102:", students.get(102))

students[105] = "Emma"
print("\nAfter adding a new student:", students)

students.pop(103)
print("\nAfter removing Roll No 103:", students)

# Check if a student exists
if 101 in students:
    print("\nRoll No 101 exists:", students[101])
