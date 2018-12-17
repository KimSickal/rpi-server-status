import threading
import time
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse

flag = False
shutdown = False

def LEDHandler():
	while(not shutdown):
		print flag
		time.sleep(1)
	

class httpHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(''+str(flag))

		pathParam = self.path[1]
		print 'ping' + pathParam

		global flag

		if(pathParam == 't'):
			flag = True
		elif(pathParam == 'f'):
			flag = False

try:
	server = HTTPServer(('', 8080), httpHandler)
	print 'Started httpserver on port 8080'
	LEDThread = threading.Thread(target=LEDHandler)
	# LEDThread.daemon = True
	LEDThread.start()
	server.serve_forever()

except KeyboardInterrupt:
	print '^C'
	global shutdown
	shutdown = True
	server.socket.close()
