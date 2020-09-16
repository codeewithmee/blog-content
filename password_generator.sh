#!/bin/bash
#simple password  generator

echo "Simple password generator"
echo "Please enter the length of the password"
read PASS_LENGTH 

for password in $(seq 1);do

	openssl rand -base64 48 | cut -c1-$PASS_LENGTH
done
