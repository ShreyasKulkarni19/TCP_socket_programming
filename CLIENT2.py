'''
#####################################################################################################################
Title : Distributed Password Cracker
Authors : Shreyas R,Shreyas Kulkarni
File name : CLIENT2.py
Last Upadted : April 18th,2020.
#####################################################################################################################
'''

#********************************************************************************************************************
#importing all the libraries
import os
from socket import *
import hashlib
#********************************************************************************************************************

#********************************************************************************************************************
#variable declaration and initialisation
host = "127.0.0.1" # set to IP address of target computer
port = 14500
addr = (host, port)
buf = 16384
buf2 = 32
password = ""
flag = 0
#********************************************************************************************************************
#Conversion of base 10 numbers to base 36 ranging from 0-9 & A-Z
def base36encode(number):
    alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base36 = ''
    if 0 <= number < len(alphabet):
        return alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return base36
#*********************************************************************************************************************

#*********************************************************************************************************************
#Creating sockets and making conncetions with the server
s = socket(AF_INET,SOCK_STREAM)
s.connect(addr)
print("Connection established with "+host)
password_hash=str(s.recv(buf).decode())
print ("The password hash is "+password_hash)
password_range_l=str(s.recv(buf2).decode())

password_range_h=str(s.recv(buf2).decode())

print ("The password range is ("+base36encode(int(password_range_l))+","+base36encode(int(password_range_h))+")")
#*********************************************************************************************************************

#*********************************************************************************************************************
#Code Logic
for x in range(int(password_range_l),int(password_range_h)):
    password = base36encode(x)
    hashvalue = hashlib.md5(password.encode())
    finalvalue = hashvalue.hexdigest()
    if str(finalvalue) == password_hash :
        flag = 1
        break
if flag==1:
    print("Password found !!!!")
    s.send(password.encode())
else:
    print("Password not found")
    s.send("Password not found".encode())

s.close()
os._exit(0)

#*********************************************************************************************************************
