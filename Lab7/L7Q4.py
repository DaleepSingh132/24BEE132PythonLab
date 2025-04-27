print("Name : Daleep Singh")
print("Roll No. : 24BEE132")
characters = input("Enter a string :")
f = {}
for character in characters :
    if character in f :
        f[character] += 1
    else :
        f[character] = 1
for keys,values in f.items() :
    print(f"{keys} : {values}")        
