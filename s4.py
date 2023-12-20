def is_binary(string):
    return all(bit in '01' for bit in string)

binary_string = "101010101"
non_binary_string = "101020101"

print(f"{binary_string} is binary: {is_binary(binary_string)}")
print(f"{non_binary_string} is binary: {is_binary(non_binary_string)}")
