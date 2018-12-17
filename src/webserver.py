import threading

import time

from PIL import Image
from PIL import ImageDraw

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from Adafruit_LED_Backpack import BicolorMatrix8x8

flag = False
shutdown = False

display = BicolorMatrix8x8.BicolorMatrix8x8()
display.begin()
display.clear()
draw = ImageDraw.Draw(image)

def LEDHandler():
	while(not shutdown):
		print flag
		if(flag):
			display.clear()
			draw.line((1, 1, 6, 6), fill=(0, 255, 0))
			draw.line((1, 6, 6, 1), fill=(0, 255, 0))

		elif(not flag):
			display.clear()
			draw.rectangle((0, 0, 7, 7), outline=(255, 0, 0), fill=(255, 255, 0))
		time.sleep(1)
	return
	

class httpHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(''+str(flag))

		pathParam = self.path[1]
		print 'ping, path: ' + pathParam

		global flag

		if(pathParam == 'a'):
			flag = True
		elif(pathParam == 'b'):
			flag = False

try:
	server = HTTPServer(('', 8080), httpHandler)
	print 'Started httpserver on port 8080'
	LEDThread = threading.Thread(target=LEDHandler)
	# LEDThread.daemon = True
	LEDThread.start()
	server.serve_forever()

except KeyboardInterrupt:
	print ' shutdown'
	global shutdown
	shutdown = True
	display.clear()
	server.socket.close()
