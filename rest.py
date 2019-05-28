# -*- coding: utf-8 -*-
import requests
import json

payload = json.dumps({"username" : "aeromexico", "password" : "4MA3r0W0lf"})
headers = {'content-type': 'application/json'}
req = requests.post('http://amex.test/api/v1/token', data=payload, headers=headers)
response = req.json()

token = response['token']
print token


pay = json.dumps({'firstname' : "Iñigo", "fatherSurname" : "González", "motherSurname" : "Pérez", "rfc" : "MARS5112263N1", "dobYear" : "1985", "dobMonth" : "7", "dobDay" : "23"})
otherheaders = {'Content-Type': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': '{0}'.format(token)}

try:
	r = requests.post('http://amex.test/api/v1/score', data=pay, headers=otherheaders)
	print r.content
except requests.exceptions.RequestException as e:
	print e
except requests.exceptions.HTTPError as err:
    print err
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)