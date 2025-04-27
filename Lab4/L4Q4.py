print("Name: Daleep Singh")
print("Roll No.: 24BEE132")
import math as m
def prime(n):
    for i in range(2, int(n // 2) + 1):
        if n % i == 0:
            return False
    return True
def perfect(n):
    per = 0
    for i in range(1, int(n // 2) + 1):
        if n % i == 0:
            per+=i
    if per == n:
        return True
    return False
def armstrong(n):
    s = str(n)
    l = len(s)
    temp = n
    arm = 0
    while(n>0):
        j = n % 10
        n = n // 10
        num = m.pow(j,l) 
        arm+=num
    if arm == temp:
        return True
    return False
def palindrome(n):
    temp = n
    pal  = 0
    while (n>0) :
        a = n % 10
        n = n // 10
        pal = (pal*10) + a
    if pal == temp :
        return True
    return False
def automorphic(n):
    temp = n
    m = str(n)
    u = len(m)
    i = 0
    n = n % (10 ** u)
    if n == temp:
        return True
    return False
      
def check(n):
    print(f"Prime: {prime(n)}")
    print(f"Perfect: {perfect(n)}")
    print(f"Armstrong: {armstrong(n)}")
    print(f"Palindrome: {palindrome(n)}")
    print(f"Automorphic: {automorphic(n)}")
n = int(input("Enter a number: "))
check(n)
