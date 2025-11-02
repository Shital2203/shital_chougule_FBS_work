#  Centered Increasing Number Pyramid

n = 5
for i in range(1, n + 1):
    # Print leading spaces
    for s in range(n - i):
        print(" ", end=" ")
    # Print increasing numbers
    for j in range(i, 2 * i):
        print(j, end=" ")
    # Print decreasing numbers
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=" ")
    print()

