print("Name:Daleep Singh")
print("Roll No.:24BEE132")
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]


result = list(map(lambda x, y: x + y, list1, list2))


print(result)
