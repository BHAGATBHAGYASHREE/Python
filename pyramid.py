'''rows = int(input("Enter number of rows: "))'''

'''for i in range(1, num_rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()'''
'''for i in range(1,num_rows + 1):
   
    for j in range(i):
     print("*  ", end=" ") 
    print()'''
 
diamond_size = int((input("enter the number")))


for i in range(1, diamond_size + 1, 2):
    spaces = " " * ((diamond_size - i) // 2)
    stars = "*" * i if i == 1 else "*" + " " * (i - 2) + "*"
    print(spaces + stars + spaces)


for i in range(diamond_size - 2, 0, -2):
    spaces = " " * ((diamond_size - i) // 2)
    stars = "*" * i if i == 1 else "*" + " " * (i - 2) + "*"
    print(spaces + stars + spaces)
