print("Name : Daleep Singh")
print("Roll No. : 24BEE132")
students = [(1,"Rahul",19),(2,"Danish",17),(3,"Shruti",20),(4,"Shreya",18),(5,"Perry",16),(6,"Kohaku",21)]
rollNo = []
names = []
ages = []
for student in students:
    rollNo.append(student[0])
    names.append(student[1])
    ages.append(student[2])
print("Roll Numbers:", rollNo)
print("Names:", names)
print("Ages:", ages)
