import os

folder = os.listdir(os.getcwd())
print(folder)

for file in folder:
    if ':' in file:
        new_file = file.split(':')
        os.rename(file, new_file[1])




