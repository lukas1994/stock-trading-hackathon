#!/usr/bin/env python

import socket


TCP_IP = '10.0.85.231'
TCP_PORT = 25000
BUFFER_SIZE = 1024
MESSAGE = '{"type":"hello","team":"LGW"}'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(MESSAGE)
data = s.recv(20)
s.close()

print "received data:", data
