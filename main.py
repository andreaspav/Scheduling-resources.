#MAIN PROGRAM - USER ENTRIES

from user import user
from job_type import jobtype
from parameters_values import parametersvalues
from check_rules import checkrules
from resources import resources
from job_queue import jobqueue


#Execute all the functions and save in the database all the features of every user
for i in range(0,4):
	user_id = user()
	title, title_parameters, title_rules, job_id = jobtype()
	arguments = parametersvalues(title, title_parameters)
	rule_num = checkrules(arguments, title, title_rules)
	job_resources, memory = resources(rule_num, title)
	jobqueue(arguments, title, title_parameters, title_rules, job_resources, user_id, job_id, memory)