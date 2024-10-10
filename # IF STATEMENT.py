# IF STATEMENT
# Generation names
age = int (input("Enter your age: \n"))
#If statement
if age>=12 and age<=27:
    print("You are Gen Z")

elif age>=28 and age <=43:
    print("You are Millennial")

elif age>=44 and age<=59:
    print("You are Gen X")

elif age>=60 and age<=78:
    print("You are a Boomer")

else:
    print("Sorry! You are out of bounds...")
