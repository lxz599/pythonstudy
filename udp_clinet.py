#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('172.0.0.1',8999))
print('I am connecting the server!')
for xx in['ABch','f���� d','h7Tq','.']:
    s.send(xx.encode('utf-8'))
    str1=s.recv(1024)
    str2=str(str1,encoding='utf-8')
    print('The original string is:',xx,'\tthe processed string is:',str2)
s.close()