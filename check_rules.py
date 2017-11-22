#Checking the corresponding rules

from json_logic import jsonLogic

def checkrules(arguments, title, title_rules):
	argument = []
	rule_num = []
	json_params1 = eval(arguments)
	args = json_params1['parameters_values']

	json_params2 = eval(title_rules)
	rules = json_params2['if']

	#Check analysis 
	if title == '1) Cloud-Based Parallel Determine_Module.':
		argument.append(int(args[0]['seeds_proteins']))
	elif title == '2) Interface Relaxation methodology.':
		argument.append(int(args[0]['Subdomain_A']))
		argument.append(int(args[0]['Subdomain_B']))
		argument.append(int(args[0]['Subdomain_C']))
	
	for j in range(0,len(argument)):
		#Check Rules
		data = { "temp" : argument[j] }
		for i in range (0,len(rules)):
			if jsonLogic(rules[i], data):
				rule_num.append(i)
				break
	
	return rule_num