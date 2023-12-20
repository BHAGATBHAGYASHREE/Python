var=10
def fun():
 
 var=3
 print(var)
 def funt():
    nonlocal var
    var=4
    print(var)   
 funt()  
 print(var) 
fun()
print(var)