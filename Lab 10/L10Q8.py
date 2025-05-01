print("Name:Daleep Singh")
print("Roll No.:24BEE132")
wordsToRemove = ['a', 'the', 'an']
with open('line1.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    words = content.split()
    nwords = [word for word in words if word.lower() not in wordsToRemove]
    ncontent = ' '.join(nwords)   
    outfile.write(ncontent)
print(f"Words 'a', 'the', and 'an' have been removed and saved to output,txt")
