#Create a class called Area
import math
#This class will contain all the
#--Funtions to calculate Area
class Area:
    
    #create a constructor
    #This is a function also referred to
    #as__int__
    def __init__(self,l,w,r,b,h) :
        self.length = l
        self.width = w
        self.Radius = r
        self.base = b
        self.height = h
        


    def AreaOfRectangle(self):
     
       
        area = self.length*self.width
        print("Area of Rectangle is: ", area ,"cm squared")

    def AreaOfCircle(self):
        
        #Pi=int(3.14)
        area=math.pi*self.Radius*self.Radius
        print("The area of the given circle is:", area ,"cm squared")
    #AreaOfCircle()

#create a TriArea

    def TriArea(self):
        area = ((self.base*self.height*)/2)
        print("The area of the given Triangle is:", area,"cm squared")
    #TriArea()

    
    #end of functions

#Create OBJECTS here outside of the class
#RObj = Area()
#CObj = Area()
#TObj = Area()



    
        

 








