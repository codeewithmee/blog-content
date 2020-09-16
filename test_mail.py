#!/usr/bin/python3

import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

	subject = 'Grab dinner this weekned'
	body = 'hello world prabhakaran'


	msg = f'Subject: {subject}\n\n{body}'
	smtp.sendmail(EMAIL_ADDRESS,'beginnerm37@gmail.com', msg)

