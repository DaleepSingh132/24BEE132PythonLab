print("Name:Daleep Singh")
print("Roll No.:24BEE132")
def frequency(string):
    string = string.lower()
    a = string.split()
    b = {}
    for i in a:
       if i in b :
          b[i] += 1
       else :
          b[i] = 1
    c = sorted(b.items())
    return c
string = input("Enter a string: ")
print(frequency(string))
