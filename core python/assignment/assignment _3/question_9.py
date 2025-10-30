# 9. Display grade based on 5 subject marks

marks = []
for i in range(5):
    marks.append(float(input(f"Enter marks of subject {i+1}: ")))

total = sum(marks)
avg = total / 5

if avg >= 75:
    grade = "Distinction"
elif avg >= 60:
    grade = "First Class"
elif avg >= 50:
    grade = "Second Class"
elif avg >= 35:
    grade = "Pass"
else:
    grade = "Fail"

print("Average =", avg)
print("Grade =", grade)
