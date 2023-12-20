class Student :
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.count+=1
    def display(self):
        print("name",self.name,"Age:",self.age)
    
obj = Student("ABC",18)   
obj.display()    
obj1=Student("xyz",30)
obj1.display()
obj6 = Student("bhagyashrer",18)   
obj6.display()    
print("count",Student.count)

