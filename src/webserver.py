from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		print 'asdf'
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write("Hello, World!")
		return

try:
	server = HTTPServer(('', 8080), handler)
	print 'Started httpserver on pirt 8080'
	server.serve_forever()

except KeyboardInterrupt:
	print '^C'
	server.socket.close()
