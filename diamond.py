
diamond_size = int((input("enter the number ")))

for i in range(1, diamond_size + 1, 2):
    spaces = " " * ((diamond_size - i) // 2)
    stars = "*" * i
    print(spaces + stars + spaces)

for i in range(diamond_size - 2, 0, -2):
    spaces = " " * ((diamond_size - i) // 2)
    stars = "*" * i
    print(spaces + stars + spaces)
