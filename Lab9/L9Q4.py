print("Name:Daleep Singh")
print("Roll No.:24BEE132")
def sumAvg(a,b,c,d,e):
    s = a+b+c+d+e
    av = s / 5
    return s,av
a,b,c,d,e = int(input("Enter the Marks of all Five Subjects:").split())
print(sumAvg(a,b,c,d,e))
