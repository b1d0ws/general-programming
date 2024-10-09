#!/bin/bash

# Ferramentas: whois, host, dig, nslookup

url=$1

# Creting Directory
echo "Do you want to create a directory called NetworkRecon? [y/N]"
read directory

if [ "${directory^^}" == "Y" ];
    then
        if [ ! -d "NetworkRecon" ]; 
        then
                mkdir NetworkRecon
                echo "[ + ] Directory NetworkRecon created"
        fi 
    cd NetworkRecon
fi

echo "Network Recon of $1" > result.txt

# whois
whois $1 > whois.txt

#host
host $1 > host.txt

#dig
dig $1 > dig.txt

#nslookup
nslookup $1 > nslookup.txt

#SPF
dig -t txt $1 > spf.txt

# Getting IPV4 Addresses
echo >> result.txt
echo "=====IPV4 Addresses=====" >> result.txt

cat nslookup.txt | egrep "([0-9]{1,3}\.){3}[0-9]+" | awk  '{print $2}' > base-ipv4.txt
sed -i -e '1,2d' base-ipv4.txt # Removing the first two lines

cat host.txt | grep "has address" | cut -d' ' -f4 >> base-ipv4.txt # Getting the 4th word

cat dig.txt | egrep "([0-9]{1,3}\.){3}[0-9]+" | grep $1 | awk 'NF>1{print $NF}' >> base-ipv4.txt # Getting just the last word

awk '!a[$0]++' base-ipv4.txt > ipv4.txt # Removing repeated lines
rm base-ipv4.txt
cat ipv4.txt >> result.txt

# Getting IPV6 Addresses
echo >> result.txt
echo "=====IPV6 Addresses=====" >> result.txt

cat host.txt | grep "has IPv6 address" | cut -d' ' -f5 > ipv6.txt

cat ipv6.txt >> result.txt

# Getting SPF
echo >> result.txt
echo "=====SPF - TXT Registers=====" >> result.txt

cat spf.txt | grep "TXT" >> result.txt
