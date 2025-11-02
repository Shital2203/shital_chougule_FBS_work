
# 2. Student Marks and Percentage


n = int(input("Enter number of students: "))
total_percent = 0

for i in range(1, n + 1):
    print(f"\nEnter marks for Student {i}:")
    total = 0
    for j in range(1, 6):
        mark = float(input(f"Subject {j}: "))
        total += mark
    percent = total / 5
    print(f"Percentage of Student {i}: {percent}%")
    total_percent += percent

avg_percent = total_percent / n
print("\nAverage percentage of all students =", avg_percent)

