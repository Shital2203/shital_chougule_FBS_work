#  Centered Decreasing-Then-Increasing Pyramid

n = 5
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print numbers in row
    for j in range(1, i + 1):
        # Print border numbers and last row
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
