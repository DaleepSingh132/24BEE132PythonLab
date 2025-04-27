print("Name:Daleep Singh")
print("Roll No.:24BEE132")
words = []  
n = int(input("Enter the range of the list: "))

for i in range(n):
    words.append(input("Enter the elements of the string: "))


filtered_words = list(filter(lambda char: len(char) <= 8, words))

print(filtered_words)
