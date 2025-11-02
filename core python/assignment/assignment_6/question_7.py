#  Alphabet pyramid pattern

rows = 5
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()
