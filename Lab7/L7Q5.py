print("Name : Daleep Singh")
print("Roll No. : 24BEE132")
p = {'milk': 30,'bread': 50,'natraj pencil': 2,'natraj rubber': 5}
q = {'apple': 5,'milk': 5,'carrot': 5,'milk': 5,'bread': 5}
totalBill = 0
for item in p:
    totalBill += p[item]*q.get(item, 0)
print(f"Total bill: Rs{totalBill:.2f}")

