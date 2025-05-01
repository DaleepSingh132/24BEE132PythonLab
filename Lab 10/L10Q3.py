print("Name:Daleep Singh")
print("Roll No.:24BEE132")
name = input("Enter Name: ")
phone = input("Enter Phone: ")
email = input("Enter Email: ")

with open("contact.vcf", "w") as f:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    f.write(f"N:{name}\n")
    f.write(f"TEL:{phone}\n")
    f.write(f"EMAIL:{email}\n")
    f.write("END:VCARD\n")
