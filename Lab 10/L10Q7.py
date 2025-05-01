print("Name:Daleep Singh")
print("Roll No.:24BEE132")
import pickle

employee = {
    'empcode': 101,
    'empname': 'John Doe',
    'Date of Joining': '2022-05-10',
    'Salary': 50000
}

with open('employee.dat', 'wb') as f:
    pickle.dump(employee, f)

with open('employee.dat', 'rb') as f:
    emp = pickle.load(f)
    print(emp)
