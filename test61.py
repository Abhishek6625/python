class Bikeshop:

     def __init__(self,stock):
         self.stock=stock

     def displyBike(self):
         print("Total Bike",self.stock)

     def rentforBike(self,q):

         if q<=0:
             print("enter the positive value or grater then zero")

         elif q>self.stock:
             print("Enter the value (less then stock)")

         else:
             self.stock=self.stock-q
             print("Total Prices",q*100)
             print("Total Bikes",self.stock)

while True:
    object=Bikeshop(100)
    uc=int(input('''
    1 Display Stock 
    2 Rent a Bike
    Exit
    
    '''))

    if uc==1:
        object.displyBike()

    elif uc==2:
        n=int(input("Enter teh Qty......"))
        object.rentforBike(n)

    else:
        break