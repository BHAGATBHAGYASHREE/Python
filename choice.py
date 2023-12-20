'''def namefun(**kwargs):
    for key, value in kwargs.items():
        print('Welcome', value, 'to ITM!')
        print(key, '=', value)

choice = input('Would you like to enter a name? ')
count = 0

if choice.lower() == 'yes':
    name = input('What is your name? ')
    namefun(name=name)
elif choice.lower() == 'no':
    choice = input('Would you like to enter an email? ')
    if choice.lower() == 'yes':
        email = input('What is your email? ')
        namefun(mail=email)
else:
    number = input('What is your phone number? ')
    namefun(number=number)
'''
def namefun(**kwargs):
    for key, value in kwargs.items():
        print('Welcome', value, 'to ITM!')
        print(key, '=', value)
details = {}
choice = input('Would you like to enter a name? ')
count = 0
if choice.lower() == 'yes':
    name = input('What is your name? ')
    details['Name']=name
    # namefun(name=name)
if count == 0:
    choice = input('Would you like to enter an email? ')
    if choice.lower() == 'yes':
        email = input('What is your email? ')
        details['Email']=email
        # namefun(mail=email)
    elif choice.lower()=='no':
        pass
if count==0:
    number = input('What is your phone number? ')
    details['Phone Number']=number
    # namefun(number=number)


print("\nFull Details:")
for key, value in details.items():
    print(f"{key} = {value}")