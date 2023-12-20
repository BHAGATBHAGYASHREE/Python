def countwords(sentence):
    words = sentence.split()
    return len(words)
userinput = input("Enter a sentence: ")
result = countwords(userinput)

print(f"Number of words in the sentence: {result}")
