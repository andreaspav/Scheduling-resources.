#Insert data into tables job_type and job_queue

import sqlite3
import datetime

def jobqueue(arguments, title, title_parameters, title_rules, job_resources, user_id, job_id, memory):

	conn = sqlite3.connect('cloudstack.db')
	c = conn.cursor()

	#Job submission date 
	submission_date = str(datetime.datetime.now())
	
	#Initialize start_execution_date with NULL
	start_execution_date = 'NULL'

	#Insert data into job_queue
	global job_queue_id
	c.execute("SELECT id FROM job_queue")
	data2 = c.fetchall()
	if len(data2) == 0:
		job_queue_id = 1000
	else:
		job_queue_id = len(data2)+1000
		
	c.execute("INSERT INTO job_queue (id, parameters_values, resources, submission_date, start_execution_date, user_id, job_id, status, credits) VALUES (?, ?, ?, ?, ?, ?, ?, 'Pending', ?)", (job_queue_id, arguments, job_resources, submission_date, start_execution_date, user_id, job_id, (sum(memory)/1024)))
	conn.commit()
	
	return user_id, job_queue_id