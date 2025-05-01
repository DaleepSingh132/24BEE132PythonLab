print("Name:Daleep Singh")
print("Roll No.:24BEE132")
import csv

data = {}

with open('students.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        total = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
        data[row['Roll No']] = {
            'Name': row['Name'],
            'Marks': [int(row['Subject1']), int(row['Subject2']), int(row['Subject3'])],
            'Total': total
        }

print(data)
