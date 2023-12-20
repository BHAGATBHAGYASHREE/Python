def cameltosnake(camelcasestring):
    result = [camelcasestring[0].lower()]

    for char in camelcasestring[1:]:
        if char.isupper():
            result.extend(['', char.lower()])
        else:
            result.append(char)

    return ''.join(result)

# Example usage:
camelcaseinput = input("Enter a CamelCase string: ")
snakecaseoutput = cameltosnake(camelcaseinput)
print(f"Converted snakecase string: {snakecaseoutput}")