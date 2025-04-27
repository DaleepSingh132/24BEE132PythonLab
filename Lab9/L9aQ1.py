print("Name:Daleep Singh")
print("Roll No.:24BEE132")
def fun():
    print("This is function fun()")

def disp():
    print("This is function disp()")

def msg():
    print("This is function msg()")


functions = [fun, disp, msg]


for func in functions:
    func()
