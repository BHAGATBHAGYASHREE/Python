string1 = "This is the first string"
string2 = "This is the second string"

words1 = set(string1.split())
words2 = set(string2.split())

uncommon_words = (words1 - words2) | (words2 - words1)
print("Uncommon words:", uncommon_words)
