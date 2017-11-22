#Insert data into user to create an account

import sqlite3
import re

def user():

	conn = sqlite3.connect('cloudstack.db')
	c = conn.cursor()

	global user_id
	correct_email = 'false'
	correct_username = 'false'
	correct_password = 'false'
	
	#user ID
	c.execute("SELECT id FROM user")
	data = c.fetchall()
	if len(data) == 0:
		user_id = 1
	else:
		user_id = len(data)+1 
	
	#Name and Surname
	name = raw_input('\nWrite your name: ')
	surname = raw_input('Write your surname: ')
		
	#Username validation check
	while (correct_username=='false'):
		username = raw_input('Username: ')
		c.execute("SELECT * FROM user WHERE username='"+username+"'")
		data = c.fetchall()
		if not data:
			correct_username = 'true'
		else:
			print ('\nThe username already exists! Write an other username.')
		
	#Password validation check
	while (correct_password=='false'):
		password = raw_input('Password: ')
		c.execute("SELECT * FROM user WHERE password='"+password+"'")
		data = c.fetchall()
		if not data:
			correct_password = 'true'
		else:
			print ('\nThe password already exists! Write an other password.')
		
	#Email validation check
	while (correct_email == 'false'):
		email = raw_input('Email: ')
		match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
		if match == None:
			print('\nWrong Email! Write again your email address.')
		else:
			correct_email = 'true'

	print '\nYour account has been successfully created!'
	c.execute("INSERT INTO user (id, name, surname, username, password, email) VALUES (?, ?, ?, ?, ?, ?)", (user_id, name, surname, username, password, email))
	conn.commit()
	
	return user_id

