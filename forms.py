'''def fun():
    name = input("Enter your name:")
    print("Welcome",name,"to ITM\nEnter your details")
fun()
def details(**kwargs):
    details={}
    for x in kwargs:
        y=input(f"Enter your {x}: ")
        details[x]=y
    return details
info=details(name="Name", age="Age", email="Email")
print("Student Details:")
for x, y in info.items():
    print(f"{x}: {y}")'''
def namefun(**kwargs):
    for key,value in kwargs.items():
        print('Welcome',value, 'to ITM!') 
        print(key,'=',value)
choice=(input('Woould you like to enter a name?'))
count=0
if choice=='yes':
    n=(input('What is your name?'))
elif choice=='no':
    choice=(input('Would you like to enter email?'))
    if choice=='yes':
        email=(input('What is your email?'))
    else:
        pass
else:
    numb=int(input('What is your phone number?'))
namefun(name=n,mail=email,number=numb)