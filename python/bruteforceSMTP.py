#!/usr/bin/python
import socket,sys,re

file = open("list.txt")
for line in file:
        tcp = socket.socket(socket.AF_INET, socker.SOCK_STREAM)
        tcp.connect((sys.argv[1], 25))
        banner = tcp.recv(1024)
        tcp.send("VRFY "+line)
        user = tcp.recv(1024)
        print user
        if re.search("252",user):
                print "User found: "+user.strip("252 2.0.0")
