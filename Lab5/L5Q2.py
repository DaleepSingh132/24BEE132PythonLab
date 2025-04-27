print("Name: Daleep Singh")
print("Roll No.:24BEE132")
import random as r
a = [r.randint(1, 100) for _ in range(20)]
print(f"Generated list: {a}")
p = []
n = int(input("Enter a number to search in the list: "))
for index, item in enumerate(a):
    if item == n: 
        p.append(index)
if p:
    print(f"The number {n} occurs at positions: {p}")
else:
    print(f"The number {n} does not appear in the list.")
