# Function to get Area of Rectangle
import math
# Defining the function
def AreaOfRectangle():
    length = int(input("Enter length:\n"))
    width =int(input("Enter width:\n"))
    area = length*width
    print("Area of Rectangle is: ", area ,"cm squared")

#outside of function
#Here, we call the function
#AreaOfRectangle()

# Area Of Circle
# Defining a Function
def AreaOfCircle():
    Radius=int(input("Enter the radius of the given circle:\n"))
    #Pi=int(3.14)
    area=math.pi*Radius*Radius
    print("The area of the given circle is:", area ,"cm squared")
AreaOfCircle()