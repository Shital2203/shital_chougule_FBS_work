# Simple Program to calculate percentage for 5 subjects.

# Get marks from the user
sub1 = float(input("Enter marks for Subject 1 (out of 100): "))
sub2 = float(input("Enter marks for Subject 2 (out of 100): "))
sub3 = float(input("Enter marks for Subject 3 (out of 100): "))
sub4 = float(input("Enter marks for Subject 4 (out of 100): "))
sub5 = float(input("Enter marks for Subject 5 (out of 100): "))

# Calculate total marks
total_marks = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage (assuming 500 is the max total marks)
percentage = (total_marks / 500) * 100

# Print the result
print(f"\nTotal Marks: {total_marks:.2f}")
print(f"Percentage: {percentage:.2f}%")
