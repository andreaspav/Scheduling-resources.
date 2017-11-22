#Deploy Virtual Machine

import urllib2
import urllib
import hashlib
import hmac
import base64
import json

def deployvm(id_so):

	baseurl='http://150.140.139.74:8282/client/api?'
	request={}
	request['command']='deployVirtualMachine'
	
	#Service Offering id
	request['serviceofferingid']=id_so
	request['templateid']='9ffca3ef-c3fa-11e6-8085-0242ac110002'
	request['zoneid']='d67c5ffa-70f9-4270-99b7-1e0ea9d53626'
	request['affinitygroupids'] = '90fa68cf-7717-4dd1-82af-91ae79156523'
	request['response']='json'
	request['apikey']='crMNsgZQUcRcoPjj5y7BjbFU2NxJJJNr9PSxiXJzHe4R-naBJYe4OFBsjln35_L89TO4J9b8vzSE3axeueq6KA'
	secretkey='22Ng2Vb3UzlSElrx9Zvfvt92jN5Y2uIaRyol2QtGe16seInyYg15DW0TPj4-pHGq2KuzyHznpHp4DtDF7Gh9Bw'

	request_str='&'.join(['='.join([k,urllib.quote_plus(request[k])]) for k in request.keys()])

	sig_str='&'.join(['='.join([k.lower(),urllib.quote_plus(request[k].lower().replace('+','%20'))])for k in sorted(request.iterkeys())])
	sig=hmac.new(secretkey,sig_str,hashlib.sha1)
	sig=hmac.new(secretkey,sig_str,hashlib.sha1).digest()
	sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest())
	sig=base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip()
	sig=urllib.quote_plus(base64.encodestring(hmac.new(secretkey,sig_str,hashlib.sha1).digest()).strip())
	req=baseurl+request_str+'&signature='+sig
	res=urllib2.urlopen(req)
	x=res.read()