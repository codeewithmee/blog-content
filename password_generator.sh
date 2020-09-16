#!/bin/bash

#simple password  generator

#!/bin/bash

#simple password  generator

echo "Simple password generator"
echo "Please enter the length of the password"
read PASS_LENGTH 

for password in $(seq 1);do

	openssl rand -base64 48 | cut -c1-$PASS_LENGTH
done

#!/usr/bin/env sh
# echo 'Generating 12-character passwords'
# for ((n=0;n<12;n++))
# do dd if=/dev/urandom count=1 2> /dev/null | uuencode -m - | sed -ne 2p | cut -c-12
# done