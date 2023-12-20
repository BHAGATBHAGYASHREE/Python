dots = [4, 3, 0, 1, 0, 3, 4]
width = 9

for i in range(len(dots)):
    for j in range(width):
        if j == dots[i] or j == width - dots[i] - 1 or (j > dots[i] and j < width - dots[i] - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
