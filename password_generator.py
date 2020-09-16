#!usr/bin/python3
import string
from random import *
characters = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter the length of the password\n"))


def password(characters):
	password=""
	for i in range(0,length):
		password += choice(characters)
	print(password)

password(characters)