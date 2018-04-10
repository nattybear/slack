from bottle import post, request, run
from sys import argv

@post('/event')
def event():
	print(request.json)
	return 'It Works!'

if __name__ == '__main__':
	if len(argv) != 2:
		argv.append('/url_verify')

	@post(argv[1])
	def url_verify():
		return request.json['challenge']

	run(host='0.0.0.0')
