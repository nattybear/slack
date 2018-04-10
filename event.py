from bottle import post, request, run
from sys import argv

if __name__ == '__main__':
	@post(argv[1])
	def url_verify():
		return request.json['challenge']

	run(host='0.0.0.0')
