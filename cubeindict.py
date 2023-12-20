
oddcubes = {}
for num in range(1, 11):
    if num % 2 != 0:  
        oddcubes[num] = num ** 3
print("Dictionary of Cubes of Odd Numbers:", oddcubes)
