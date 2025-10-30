amount = int(input("Enter amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("Minimum number of notes:")
for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(note, "x", count)
