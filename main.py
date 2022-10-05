# file handling: navigate, rename, move, copy, remove
# how to keep your desktop organized

import os

mypath = "C:\\Users\\Geisti\\Desktop\\NFT"

print(os.getcwd())

os.chdir(my_path)

print(os.getcwd())

for file in os.listdir():
    print(file)
    name, ext = os.path.splitext(file)
    print(name)
    print(ext)