num_rows = int(input("Enter the number of rows for the right-angled triangle: "))
for i in range(1, num_rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()