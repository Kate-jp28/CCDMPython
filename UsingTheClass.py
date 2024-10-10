#as a user
from classes import Area

#create choices.
choice = int(input("Enter your choice 1,2 or 3:\n"))
#IF STATEMENT
if choice == 1:
    l = int(input("Enter length:\n"))
    w = int(input("Enter width:\n"))
    print("AreaOfRectangle")

elif choice==2:
    r = int(input("Enter Radius:\n"))
    print("AreaOfCircle")

elif choice==2 :
    b = int(input("Enter base:\n"))
    h = int(input("Enter height:\n"))
    print("TriArea")

else:
    print("Sorry!Invalid Option") 

l = int(input("Enter length:\n"))
w = int(input("Enter width:\n"))
r = int(input("Enter Radius:\n"))
b = int(input("Enter base:\n"))
h = int(input("Enter height:\n"))

#Create object and assign values
RObj = Area(l,w,0)
#use object to access the AreaOfRectangle Function
RObj.AreaOfRectangle()  #test this first

#create object and assign values
CObj = Area(0,0,r)
#use object to access the AreaOfCircle Function
CObj.AreaOfCircle()    

#create object and assign values
TObj = Area(0,b,h)
#use object to access the TriArea Function
TObj.TriArea()