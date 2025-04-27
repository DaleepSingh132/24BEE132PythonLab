print("Name: Daleep Singh")
print("Roll No.: 24BEE132")
import math as m
def fac(n):
    r = 1
    for j in range(1, n + 1):
        r *= j
    return r
d = int(input("Enter the value of X(in degree):"))
x = d*3.14159/180
sinX = 0
for i in range (1, 15, 2):
    a = m.pow(x, i)
    b = a / fac(i)
    if (i // 2) % 2 == 0 :
        b = b
    else :
        b = b*(-1)
    sinX += b
print(f"The sin of {d} is approximately: {sinX}")  
