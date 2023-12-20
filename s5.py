from collections import Counter

def least_frequent_char(string):
    char_count = Counter(string)
    return min(char_count, key=char_count.get)

input_string = "hello world"
result = least_frequent_char(input_string)
print(f"The least frequent character is: {result}")
