print("Name : Daleep Singh")
print("Roll No. : 24BEE132")
employees = {1:{101:80000,102:35000,107:25000,105:60000},2:{111:40000,112:35000,116:70000,104:20000}}
for depart,emp in employees.items() :
    minSalary = min(emp.values()) 
    maxSalary = max(emp.values()) 
    print(f"Department {depart} - Min Salary: {minSalary}, Max Salary: {maxSalary}")
