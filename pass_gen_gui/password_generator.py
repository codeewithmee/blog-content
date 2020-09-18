#!usr/bin/python3
import string
from random import *



def pwd(length):
	characters = string.ascii_letters + string.digits + string.punctuation
	password=""
	for i in range(0,int(length)):
		password += choice(characters)
	return password

