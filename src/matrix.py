import time

from Adafruit_LED_Backpack import BicolorMatrix8x8

from PIL import Image
from PIL import ImageDraw

RED = (255, 0, 0)
GRN = (0, 255, 255)
YEL = (255, 255, 0)
BLK = (0, 0, 0)

bitmapImage = {
	# 'success': [
	# 	[BLK, BLK, GRN, GRN, GRN, GRN, BLK, BLK, ],
	# 	[BLK, GRN, GRN, GRN, GRN, GRN, GRN, BLK, ],
	# 	[GRN, GRN, GRN, GRN, GRN, GRN, GRN, GRN, ],
	# 	[GRN, GRN, GRN, GRN, GRN, GRN, GRN, GRN, ],
	# 	[GRN, GRN, GRN, GRN, GRN, GRN, GRN, GRN, ],
	# 	[GRN, GRN, GRN, GRN, GRN, GRN, GRN, GRN, ],
	# 	[BLK, GRN, GRN, GRN, GRN, GRN, GRN, BLK, ],
	# 	[BLK, BLK, GRN, GRN, GRN, GRN, BLK, BLK, ],
	# ]
	'success': [
		BLK, BLK, GRN, GRN, GRN, GRN, BLK, BLK,
		BLK, GRN, GRN, GRN, GRN, GRN, GRN, BLK,
		GRN, GRN, GRN, GRN, GRN, GRN, GRN, GRN,
		GRN, GRN, GRN, GRN, GRN, GRN, GRN, GRN,
		GRN, GRN, GRN, GRN, GRN, GRN, GRN, GRN,
		GRN, GRN, GRN, GRN, GRN, GRN, GRN, GRN,
		BLK, GRN, GRN, GRN, GRN, GRN, GRN, BLK,
		BLK, BLK, GRN, GRN, GRN, GRN, BLK, BLK,
	]
}

class matrix (object):
	def __init__(self):
		self.display = BicolorMatrix8x8.BicolorMatrix8x8()
		self.frameIndex = 0
		self.currMode = ''
		self.display.begin()
		self.display.clear()

	def _showImage(self, image, duration):
		self.display.clear()
		if(duration < 0):
			# self.display.set_image(image)
			self.display.set_pixel(1,1,BicolorMatrix8x8.RED)
			self.frameIndex = 0
		elif(self.frameIndex < duration):
			self.display.set_image(image)
			self.frameIndex += 1
		else:
			self.display.create_blank_image()
			self.frameIndex = 0
		self.display.write_display()

	def _initImage(self, image, duration):
		self.display.clear()
		if(duration == 0):
			self.display.create_blank_image()
		else:
			self.display.set_image(image)
		self.frameIndex = 0
		self.display.write_display()

	def disableImage(self):
		self.display.clear()
		self.display.create_blank_image()
		self.display.write_display()
		self.currMode = ''
		self.frameIndex = 0
		time.sleep(1)

	def playImage(self, imageName, fps = 1, duration = -1):
		image = Image.new('RGB', (8, 8))
		image.putdata(bitmapImage[imageName])
		if(self.currMode == imageName):
			self._showImage(image, duration)
		else:
			self.currMode = imageName
			self._initImage(image, duration)
		time.sleep(1 / fps)




			