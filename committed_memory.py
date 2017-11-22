#Keep the committed memory of zone from account "pavlopoulos"

import urllib2
import urllib
import hashlib
import hmac
import base64
import json

def committedmemory():

	service_offering_id = []
	#List of Virtual Machines from account "pavlopoulos"
	baseurl='http://150.140.139.74:8282/client/api?'
	request={}
	request['command']='listVirtualMachines'
	request['account']='pavlopoulos'
	request['domainid']='8bb59016-c3fa-11e6-8085-0242ac110002'
	request['response']='json'
	request['apikey']='-vOcQxGQ8HP08PQfvpQYoVKM-WUi0Of9wxqQx916k16lUM7gKLfgsBr8mqHEAsn0FhMvWyhhNYp2RvUY6edaZg'
	secretkey='HyO7U9TxZzUc8WDgX-N_5eq5ZwRKnBGougDfGFyeJcnQ7s0ton7ayh81zheOYUaT4S_ZelEf4FZ5YrvDL2fd4Q'

	request_str = '&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])

	sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
	sig=hmac.new(secretkey,sig_str,hashlib.sha1)
	sig=hmac.new(secretkey,sig_str,hashlib.sha1).digest()
	sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest())
	sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip()
	sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
	req=baseurl+request_str+'&signature='+sig
	res=urllib2.urlopen(req)
	x=res.read()

	#JSON
	data=json.loads(x)
	data = data['listvirtualmachinesresponse']
	if len(data)>0:
		count = data['count']
		vm = data['virtualmachine']
		committed_ram = 0
		#Keep the total memory RAM of all running virtuals machine from account "pavlopoulos"
		for i in range(0, count):
			virtual_machine = vm[i]
			committed_ram = committed_ram + virtual_machine['memory']/1024
	else:
		committed_ram = 0

	return committed_ram
