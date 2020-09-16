#!/bin/bash

#find what are the devices conected in your network
echo "Enter your the Subnet"
read SUBNET

for ip in $(seq 1 254);
do
	ping -c 1 $SUBNET.$ip | grep "bytes from" | cut -d " " -f 4 | cut -d ":" -f 1 &
done

