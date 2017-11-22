#Compute the Resources that each job need.

def resources(rule_num, title):

	memory = []
	for j in range(0,len(rule_num)):
		#Compute Resources
		if title == '1) Cloud-Based Parallel Determine_Module.':
			vm_number = 1
			cpu_speed = 2000
			memory.append(4096)
			if rule_num[j]==0:
				cpu_number = 1
			elif rule_num[j]==1:
				cpu_number = 2
			elif rule_num[j]==2:
				cpu_number = 3
		elif title == '2) Interface Relaxation methodology.':
			vm_number = 3
			cpu_number = 1
			cpu_speed = 2000
			if rule_num[j]==0:
				memory.append(1024)
			elif rule_num[j]==1:
				memory.append(2048)
			elif rule_num[j]==2:
				memory.append(4096)
		
	#Resources as JSON
	job_resources = '{"resources": [{"vm_number": ' + str(vm_number) + ',"cpu_number": ' + str(cpu_number) + ', "cpu_speed": ' + str(cpu_speed) + ', "memory": ' + str(memory) + '}]}'
	
	return job_resources, memory

