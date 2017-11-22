#Show the analysis in a list on screen. Selection by the user of the analysis
#wishing and storing the corresponding parameters and rules into the table job_type.

import sqlite3

def jobtype():
	
	conn = sqlite3.connect('cloudstack.db')
	c = conn.cursor()
	
	#job ID
	global job_id
	c.execute("SELECT id FROM job_type")
	data1 = c.fetchall()
	if len(data1) == 0:
		job_id = 100
	else:
		job_id = len(data1)+100
	
	#Analysis array
	analysis = []
	analysis.append('1) Cloud-Based Parallel Determine_Module.')
	analysis.append('2) Interface Relaxation methodology.')

	print '\n----------------------------------------------'
	for i in range(len(analysis)):
		print analysis[i]
	print '----------------------------------------------'

	correct_user_analysis = 'false'
	#Analysis validation check
	while (correct_user_analysis == 'false'):
		user_analysis = raw_input('\nGive the number of the analysis: ')
		try:
			user_analysis = int(user_analysis)
		except ValueError:
			print('You must give an int value!')
		if (user_analysis > 0 and user_analysis <= len(analysis)):
			correct_user_analysis = 'true'

	title = analysis[user_analysis-1]
	
	#Store parameters and rules as JSON
	#Parameters array
	parameters = []

	param1 = '{"parameters": [{ "title": "Seeds_number: Number of seeds proteins","type": "Parameter type: int"}]}'
	parameters.append(param1)

	param2_1 = '{"parameters": [{"title": "Subdomain A","type": "Parameter type: int"},'
	param2_2 = '{"title": "Subdomain B","type": "Parameter type: int"},'
	param2_3 = '{"title": "Subdomain C","type": "Parameter type: int"}]}'
	param2 = param2_1 + param2_2 + param2_3
	parameters.append(param2)

	title_parameters = parameters[user_analysis-1]

	#Rules array
	rules = []
	rule1 = { "if" : [
		{ "and" : [
		  {">" : [ { "var" : "temp" }, 0 ]},
		  {"<=" : [ { "var" : "temp" }, 10 ] }
		] },
		{ "and" : [
		  {">" : [ { "var" : "temp" }, 10 ]},
		  {"<=" : [ { "var" : "temp" }, 25 ] }
		] },
		{ "and" : [
		  {">" : [ { "var" : "temp" }, 25 ]}
		] }
	 ]}
	rule1 = str(rule1)
	rules.append(rule1)

	rule2 = { "if" : [
		{ "and" : [
		  {">" : [ { "var" : "temp" }, 0 ]},
		  {"<=" : [ { "var" : "temp" }, 75000 ] }
		] },
		{ "and" : [
		  {">" : [ { "var" : "temp" }, 75000 ]},
		  {"<=" : [ { "var" : "temp" }, 150000 ] }
		] },
		{ "and" : [
		  {">" : [ { "var" : "temp" }, 150000 ]}
		] }
	 ]}
	rule2 = str(rule2)
	rules.append(rule2)

	title_rules = rules[user_analysis-1]
	
	c.execute("INSERT INTO job_type (id, title, parameters, rules) VALUES (?, ?, ?, ?)", (job_id, title, title_parameters, title_rules))
	conn.commit()
	
	return title, title_parameters, title_rules, job_id