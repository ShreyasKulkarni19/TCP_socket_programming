'''
###############################################################################################
Title : Distributed Password Cracker
Authors : Shreyas R,Shreyas Kulkarni
File name : SERVER.py
Last Upadted : April 18th,2020.
###############################################################################################
'''

#**********************************************************************************************
#importing all the libraries
import os
import random
from socket import *
import hashlib
import time
#**********************************************************************************************

#**********************************************************************************************
#variable declaration and initialisation
host = ""
port1 = 13000
port2 = 14500
buf = 1024
password = ""
addr1 = (host,port1)
addr2 = (host,port2)
#**********************************************************************************************

#**********************************************************************************************
#Creating sockets and making connections with the client
Sock1 = socket(AF_INET,SOCK_STREAM)
Sock1.bind(addr1)
Sock1.listen(10)
Sock2 = socket(AF_INET,SOCK_STREAM)
Sock2.bind(addr2)
Sock2.listen(10)
print("Waiting for client 1 to start.....")
print("Waiting for client 2 to start.....")
(newsock1,addr1) = Sock1.accept()
(newsock2,addr2) = Sock2.accept()
print("Connection established from " +str(addr1))
print("Connection established from " +str(addr2))
#**********************************************************************************************

#**********************************************************************************************
#Code logic

password = str(input("Enter a 4 digit password with capital letters and digits: "))
print("The password is : "+password)
hashvalue = hashlib.md5(password.encode())
finalvalue = hashvalue.hexdigest()
print("The hex representation of password = "+finalvalue)
range1_l = "0"
range1_h = "839807"
range2_l = "839808"
range2_h = "1679615"
newsock1.send(finalvalue.encode())
newsock1.send(range1_l.encode())

newsock2.send(finalvalue.encode())
newsock2.send(range2_l.encode())
time.sleep(2)
newsock1.send(range1_h.encode())
newsock2.send(range2_h.encode())
print("Hash and range sent")
print("Waiting for clients to process and find the password ......")
time.sleep(2)
print("hello")
reply1 = newsock1.recv(buf).decode()
reply2 = newsock2.recv(buf).decode()
if reply1 != "Password not found" :
    print("Password found !!!")
    print("Password found by client 1 : "+reply1)
if reply2 != "Password not found" :
    print("Password found !!!")
    print("Password found by client 2 : "+reply2)
Sock1.close()
Sock2.close()
os._exit(0)
 
#*********************************************************************************************
