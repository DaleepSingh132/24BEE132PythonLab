print("Name:Daleep Singh")
print("Roll no.:24BEE132")
s1=int(input("Enter the marks of first subject:"))
s2=int(input("Enter the marks of second subject:"))
s3=int(input("Enter the marks of third subject:"))
t=s1+s2+s3
a=t/3
print("Total:",t)
print("Average:",a)
if(s1&s2&s3<=39):
    print("FAIL!")
else:
    print("PASS")
print("Grade for first subject is:")   
if(s1>=80):
    print("O")
elif(s1>=70):
    print("A+")
elif(s1>=60):
    print("A")
elif(s1>=55):
    print("B+")
elif(s1>=50):
    print("B")
elif(s1>=45):
    print("C")
elif(s1>=40):
    print("P")
else:
    print("NA")
print("Grade for second subject is:")   
if(s2>=80):
    print("O")
elif(s2>=70):
    print("A+")
elif(s2>=60):
    print("A")
elif(s2>=55):
    print("B+")
elif(s2>=50):
    print("B")
elif(s2>=45):
    print("C")
elif(s2>=40):
    print("P")
else:
    print("NA")
print("Grade for third subject is:")   
if(s3>=80):
    print("O")
elif(s3>=70):
    print("A+")
elif(s3>=60):
    print("A")
elif(s3>=55):
    print("B+")
elif(s3>=50):
    print("B")
elif(s3>=45):
    print("C")
elif(s3>=40):
    print("P")
else:
    print("NA")
        
    
    
