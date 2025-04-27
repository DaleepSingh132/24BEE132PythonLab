print("Name: Daleep Singh")
print("Roll No.: 24BEE132")
def count(s):
    a = 0
    d = 0
    for char in s:
        if char.isalpha():
            a += 1
        elif char.isdigit():
            d += 1
    
    return a,d
s= input("Enter a string:")
a,d = count(s)
print(f"Alphabets: {a}, Digits: {d}")
