from urllib.request import urlopen, Request
from json import dumps

def send(url, text):
	headers = {'Content-type': 'application/json'}
	dic = {'text': text}
	json = dumps(dic)
	data = json.encode('utf-8')
	req = Request(url, data=data, headers=headers)
	res = urlopen(req)
	res.close()
