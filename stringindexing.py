def checkOccurence(str,ch,choice):
    if choice==1:
        if ch in str:
            return str.index(ch)
        else:
            return -1
    elif choice==2:
        index = 0
        for i in range(len(str)):
            if str[i] == ch:
                index = i
                return index
        
        return -1
    

str = input("Enter string: ")
choice = int(input("1)String\n2)Char\nEnter choice: "))

if choice==1:
    char = input("Enter substring to find for: ")
    index = checkOccurence(str,char,choice)
    if index==-1:
        print(f"'{char}' not found in string '{str}'")
    else:
        print(f"'{char}' found from position {index} in '{str}'")
elif choice==2:
    count = 0
    char = input("Enter character to find for: ")
    index = checkOccurence(str,char,choice)
    for i in range(len(str)):
        if str[i]==char:
            count+=1
    if index==-1:
        print(f"'{char}' not found in string '{str}'")
    else:
        print(f"'{char}' found at position {index} in '{str}', total of {count} times in string")