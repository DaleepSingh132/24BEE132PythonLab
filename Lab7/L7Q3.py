print("Name : Daleep Singh")
print("Roll No. : 24BEE132")
employees = {1:{20000:101,80000:102,35000:107,25000:105},2:{10000:111,40000:112,35000:116,70000:104}}
for depart,emp in employees.items() :
    minSalary = min(emp.keys()) 
    maxSalary = max(emp.keys()) 
    print(f"Department {depart} - Min Salary: {minSalary}, Max Salary: {maxSalary}")
