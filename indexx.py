#list=input("Enter a list of numbers separated by spaces: ").split()
#my_list=[int(num) for num in list]
'''search_value=int(input("Enter the value to search for: "))
indices=[]
count=0
for i in range(len(my_list)):
    if my_list[i]==search_value:
        indices.append(i)
        count+=1
print(f"The value {search_value} exists at indices: {indices}")
'''print(f"The value {search_value} is repeated {count} times.")
list = [4, 2, 5, 2, 7, 2, 8, 2]
search_val=2
indices=[]
count=0
for i in range(len(list)):
    if list[i]==search_val:
        indices.append(i)
        count+=1
print(f"The value {search_val} exists at indices: {indices}")
print(f"The value {search_val} is repeated {count} times.")'''