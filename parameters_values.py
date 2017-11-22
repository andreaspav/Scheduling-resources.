#Display the parameters on the user's screen and import the appropriate values.

def parametersvalues(title, title_parameters):
	arg = []
	correct_parameter = 'false'
	json_params = eval(title_parameters)
	x = json_params['parameters']

	#Parameters values and Check if the type is int
	#Store the arguments as JSON
	if title == '1) Cloud-Based Parallel Determine_Module.':
		while correct_parameter == 'false':
			a = raw_input('\nGive the number of the seeds proteins:\n')
			try:
				a = int(a)
			except ValueError:
				print('You must give an int value!')
			if type(a)==int:
				correct_parameter = 'true'
				a = str(a)
				arg.append(a)
		arguments = '{"parameters_values": [{"seeds_proteins": ' + arg[0] + '}]}'
	elif title == '2) Interface Relaxation methodology.':
		for i in range(0,len(x)):
			correct_parameter = 'false'
			while correct_parameter == 'false':
				print '\nGive the ', x[i]['title'], ':'
				a = raw_input()
				try:
					a = int(a)
				except ValueError:
					print('You must give an int value!')
				if type(a)==int:
					correct_parameter = 'true'
					a = str(a)
					arg.append(a)
		arguments = '{"parameters_values": [{"Subdomain_A": ' + arg[0] + ',"Subdomain_B": ' + arg[1] + ', "Subdomain_C": ' + arg[2]+ '}]}'

	return arguments