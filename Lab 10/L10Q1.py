print("Name:Daleep Singh")
print("Roll No.:24BEE132")
import csv

with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'])
    writer.writerow([1, 'Alice', 85, 90, 92])
    writer.writerow([2, 'Bob', 78, 88, 84])
