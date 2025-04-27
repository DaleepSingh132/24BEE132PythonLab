print("Name:Daleep Singh")
print("Roll no.:24BEE132")
s = input("Enter a string: ")
i = 0
l = len(s)
r = ""
u = ""
t = ""
while i < l:
    if ord(s[i]) >= 97 and ord(s[i]) <= 122:
        u += chr(ord(s[i]) - 32)
    else:
        u += s[i]
    i += 1
print("Upper case:",u)
i = 0
while i < l:
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        r += chr(ord(s[i]) + 32)
    else:
        r += s[i]
    i += 1
print("Lower case:",r)
i = 0
while i < l:
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        t += chr(ord(s[i]) + 32)
    elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
        t += chr(ord(s[i]) - 32)
    else:
        t += s[i]
    i += 1
    
print("Toggled case:",t)
