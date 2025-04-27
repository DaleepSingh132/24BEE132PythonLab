print("Name:Daleep Singh")
print("Roll no.:24BEE132")
x1=int(input("Enter the x coordinate of first point:"))
y1=int(input("Enter the y coordinate of first point:"))
x2=int(input("Enter the x coordinate of second point:"))
y2=int(input("Enter the y coordinate of second point:"))
x3=int(input("Enter the x coordinate of third point:"))
y3=int(input("Enter the y coordinate of third point:"))
if((y2-y1)/(x2-x1)==(y3-y2)/(x3-x2)==(y3-y1)/(x3-x1)):
    print("All points fall on a straight line")
else:
    print("All points don't fall on a straight line")
