#  Pascal’s Triangle pattern

rows = 4
for i in range(rows):
    val = 1
    for j in range(rows - i + 1):
        print(" ", end="")
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()

