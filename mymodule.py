class Addition :
    def add(self,x,y):
        print(x+y)
class Subtraction:        
    def sub(self,x,y):
        print(x-y)   
class Div:
    def multi(self,x,y):
        print(x*y)
    def div(self,x,y):    
        print(x/y)
aa = Addition()        
if __name__=='__main__':
    print(aa.add(2,3))
else:
    print("called module is ",__name__)    
    print('excuse me!')