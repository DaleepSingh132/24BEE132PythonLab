print("Name:Daleep Singh")
print("Roll No.:24BEE132")
import os
import shutil

os.makedirs('destination_folder', exist_ok=True)
shutil.copy('source_folder/sample.txt', 'destination_folder/sample.txt')
