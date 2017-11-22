import sqlite3

conn = sqlite3.connect('cloudstack.db')
c = conn.cursor()

#CREATE and INSERT into table cloudstack_service_offerings the service offerings that cloudstack provides.
c.execute('DROP TABLE cloudstack_service_offerings')
c.execute('CREATE TABLE IF NOT EXISTS cloudstack_service_offerings(id VARCHAR(256), cpu INT, cores INT, ram INT, PRIMARY KEY (id))')

c.execute("INSERT INTO cloudstack_service_offerings VALUES ('acd76ab0-2a3b-46be-aa83-7655943e81e5', 2000, 1, 1024)")
c.execute("INSERT INTO cloudstack_service_offerings VALUES ('16b66718-b5d5-4d61-944f-acdd63e6db6d', 2000, 1, 2048)")
c.execute("INSERT INTO cloudstack_service_offerings VALUES ('c018eff3-5754-4b0e-bead-115548cc73fd', 2000, 1, 4096)")
c.execute("INSERT INTO cloudstack_service_offerings VALUES ('6ab68b4c-1998-410f-b7c6-28b8d795bb00', 2000, 1, 4096)")
c.execute("INSERT INTO cloudstack_service_offerings VALUES ('e4a93b3a-0ec5-4089-8324-79d920575417', 2000, 2, 4096)")
c.execute("INSERT INTO cloudstack_service_offerings VALUES ('1c429b6f-c848-4f8c-a441-132546b19fa1', 2000, 3, 4096)")

conn.commit()

c.execute('DROP TABLE user')
c.execute('DROP TABLE job_type')
c.execute('DROP TABLE job_queue')

#Create tables user, job_type, job_queue
c.execute('CREATE TABLE IF NOT EXISTS user(id INT, name VARCHAR(256), surname VARCHAR(256), username VARCHAR(256), password VARCHAR(256), email VARCHAR(45), PRIMARY KEY (id))')
c.execute('CREATE TABLE IF NOT EXISTS job_type(id INT, title VARCHAR(256), parameters LONGTEXT, rules LONGTEXT, PRIMARY KEY (id))')
c.execute('CREATE TABLE IF NOT EXISTS job_queue(id INT, parameters_values LONGTEXT, resources LONGTEXT, submission_date VARCHAR(45), start_execution_date VARCHAR(45), user_id INT, job_id INT, status VARCHAR(45) NOT NULL, credits float unsigned, PRIMARY KEY (id), FOREIGN KEY (user_id) REFERENCES user(id), FOREIGN KEY (job_id) REFERENCES job_type(id))')
conn.commit()