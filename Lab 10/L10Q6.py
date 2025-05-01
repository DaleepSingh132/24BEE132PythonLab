print("Name:Daleep Singh")
print("Roll No.:24BEE132")
with open('line1.txt', 'r') as fl1, open('line2.txt', 'r') as fl2, open('linef.txt', 'w') as fl3:
    ch1 = fl1.read(1)
    ch2 = fl2.read(1)
    
    while ch1 or ch2:
        while ch1 and ch1 != ".":
            fl3.write(ch1)
            ch1 = fl1.read(1)
        if ch1 == ".":
            fl3.write(ch1)
            ch1 = fl1.read(1)
        while ch2 and ch2 != ".":
            fl3.write(ch2)
            ch2 = fl2.read(1)
        if ch2 == ".":
            fl3.write(ch2)
            ch2 = fl2.read(1)
