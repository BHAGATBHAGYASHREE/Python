def countvowels(inputstring):
    vowels = "aeiouAEIOU"
    vowelcount = 0
    for char in inputstring:
        if char in vowels:
            vowelcount += 1
    return vowelcount
userinput = input("Enter a string: ")
result = countvowels(userinput)

print(f"Number of vowels in the string: {result}")
