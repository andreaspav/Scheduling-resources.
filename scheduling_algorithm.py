import sqlite3
from committed_memory import committedmemory
from deploy_vm import deployvm
import time
import datetime

conn = sqlite3.connect('cloudstack.db')
c = conn.cursor()

while True:
	jobs_id = []
	jobs_resources = []
	jobs_credits = []
	#service_offering = []
	
	#Jobs with status Pending
	c.execute("SELECT id, resources, credits FROM job_queue WHERE status='Pending'")
	jobs_Q = c.fetchall()

	for i in range(0, len(jobs_Q)):
		jobs_id.append(jobs_Q[i][0])
		jobs_resources.append(jobs_Q[i][1])
		jobs_credits.append(jobs_Q[i][2])

	#For all Pending jobs
	while jobs_Q:
		service_offering = []
		#Find job with minimum credits
		next_job = jobs_credits.index(min(jobs_credits))
		res = jobs_resources[next_job]
		json_params1 = eval(res)
		res = json_params1['resources']
		job_vm = res[0]['vm_number']
		job_cpu = res[0]['cpu_speed']
		job_cpu_cores = res[0]['cpu_number']
		job_memory = res[0]['memory']
		ram = sum(res[0]['memory'])/1024

		#Keep the available memory RAM from CloudStack
		committed_ram = committedmemory()
		available_ram = 7.75 - committed_ram
		
		#Check if there is available memory in CloudStack
		if (available_ram-ram)>=0:
			for j in range(0,len(job_memory)):
				c.execute("SELECT id FROM cloudstack_service_offerings WHERE cpu='"+str(job_cpu)+"' AND cores='"+str(job_cpu_cores)+"' AND ram='"+str(job_memory[j])+"' ")
				service_offering.append(c.fetchall())
				#Deploy VM
				deployvm(service_offering[j][0][0])
			c.execute("UPDATE job_queue SET status='Running' WHERE id=='"+str(jobs_id[next_job])+"'")
			conn.commit()
			print '\nThe job with id=' + str(jobs_id[next_job]) + ' is executing now!'
			c.execute("UPDATE job_queue SET start_execution_date='"+str(datetime.datetime.now())+"' WHERE id=='"+str(jobs_id[next_job])+"'")
			conn.commit()
			available_ram = available_ram-ram
			
			#Remove job from queue
			jobs_Q.remove(jobs_Q[next_job])
			jobs_credits.remove(jobs_credits[next_job])
			jobs_resources.remove(jobs_resources[next_job])
			jobs_id.remove(jobs_id[next_job])
		else:
			print '\nThe job with id=' + str(jobs_id[next_job]) + ' cannot execute now!'
			print '---Please wait to be available the appropriate memory!---'
			for k in range(0,len(jobs_credits)):
				if jobs_credits[k]>0:
					jobs_credits[k] = jobs_credits[k] - 0.1
				else:
					jobs_credits[k] = 0
				c.execute("UPDATE job_queue SET credits='"+str(jobs_credits[k])+"' WHERE id=='"+str(jobs_id[k])+"'")
				conn.commit()
			jobs_Q = False
	time.sleep(60)
