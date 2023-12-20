#to calculate parking charges of a vehicle. Enter the type of vehicle as a character (c for car , b for bus etc) and no of hrs, then calculate charges as given below 
#truck/bus-20rupees per hr , car-10rupees per hr , scooter/cycle/bile - 5rupees per bus
vehicles=input("enter the vehicle type c for car b for bus :")
checkin=float(input("enter the  checkin hour :"))
checkout=float(input("enter the checkout hour :"))
hours=checkout-checkin
if vehicles =='c': 
  if hours>=3:
     perhr=20
  else:  
    perhr=10
elif vehicles =='b':
    if hours>=3:
     perhr=30
    else: 
     perhr=20
else:
    if hours>=3:
     perhr=10
    else: 
     perhr=5
    
total=hours*perhr

print("Parking charges for", vehicles, "for", hours, "hours:",total,"rupees.")
print('---------------------------------------------------------------------------------------------------------')
print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,RECEIPT,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
print("total number of hours",hours)
print("total number of charge ",total)
print('---------------------------------------------------------------------------------------------------------')



