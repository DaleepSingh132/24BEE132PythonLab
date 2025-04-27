print("Name:Daleep Singh")
print("Roll No.:24BEE132")
def createList(lst1,lst2):
    flst = set(lst1)
    slst = set(lst2)
    rlst = flst & slst
    return rlst
lst1 = [ 2, 3, 7, 8, 56 ]
lst2 = [ 8, 3, 4, 8, 2, 4 ]
print(createList(lst1,lst2))
