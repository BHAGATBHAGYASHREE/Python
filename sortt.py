def sortstringsbylength(stringlist):
    return sorted(stringlist, key=len)
numstrings = int(input("Enter the number of strings: "))
inputstrings = [input(f"Enter string {i + 1}: ") for i in range(numstrings)]
sortedstrings = sortstringsbylength(inputstrings)
print("Sorted strings by length:")
for string in sortedstrings:
    print(string)
