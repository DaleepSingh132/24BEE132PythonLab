print("Name: Daleep Singh")
print("Roll No.: 24BEE132")
def f(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r
def nCr(n, r):
    return f(n) / (f(r) * f(n - r))
def nPr(n, r):
    return f(n) / f(n - r)
n = int(input("Enter n:"))
r = int(input("Enter r:"))
print(f"nCr:", nCr(n, r))
print(f"nPr:", nPr(n, r))
