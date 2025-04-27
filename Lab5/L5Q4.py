print("Name: Daleep Singh")
print("Roll No.:24BEE132")
import random as r
a = [r.randint(-100, 100) for _ in range(30)]
print(f"Generated list: {a}")
p = []
n = []
for item in a :
    if item < 0 :
        n.append(item)
    elif item > 0 :
        p.append(item)
print(f"Positive list: {p}")
print(f"Negative list: {n}")
