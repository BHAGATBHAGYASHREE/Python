'''list'''
lists=['bhagyashree',1,2,3]
print(lists)
'''to add at the end '''
lists.append(11)
print(lists)
'''to add multiple value'''
lists.extend([10,'bhagat'])
print(lists)
'''it will delete the default last value'''
lists.pop()
print(lists)
'''to remove it by index'''
lists.pop(1)
print(lists)
'''it will reverse '''
lists.reverse()
print(lists)
'''it will insert element on given index'''
lists.insert(2,'hello')
print(lists)
'''to remove it by item'''
lists.remove('hello')
print(lists)
'''it will print in ascending order'''
numlist=[5,3,6,7,5,9]
print(numlist)
'''it will print in descending order'''
numlist.sort(reverse=True)
print(numlist)
