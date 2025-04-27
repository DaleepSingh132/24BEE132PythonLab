print("Name : Daleep Singh")
print("Roll No. : 24BEE132")
names= [("Rahul",), ("Danish",), "Shruti", "Shreya", ("Perry",), "Kohaku"]
boys = 0
girls = 0
print(names)
for name in names :
    if isinstance(name, tuple):
        boys += 1
    elif isinstance(name, str):
        girls += 1
print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")
