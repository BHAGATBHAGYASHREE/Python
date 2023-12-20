str = input("Enter string : ")
ind= int(input("Enter the index to be Removed:"))
a= ""
for i in range(0,len(str)):
     if(i != ind):
         a += str[i]
print(a)


