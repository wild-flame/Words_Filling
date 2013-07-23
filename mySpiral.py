import Image,ImageDraw,ImageFont,os
from math import pi,sin,cos

class SpireShape(object):
	def __init__(self, draw):
		self.draw = draw
		self.line_width = 1
		self.line_color = (0,0,0)
		self.current_point = (0,0)

	def setPoints(self,points):
		self.points = points

	def setLineWidth(self,line_width):
		self.line_width = line_width

	def setLineColor(self,line_color):
		self.line_color = line_color

	def moveto(self, p):
		self.current_point = p

	def lineto(self, p):
		self.draw.line((self.current_point, p),width=self.line_width, fill=self.line_color)
		self.current_point = p

	def point(self, p):
		self.draw.point(p,fill=self.line_color)
		self.current_point = p

	def text(self, p, string):
		self.draw.text(p, string, fill=255,font=self.font)

	def setTextFont(self):
		self.font = ImageFont.truetype("FreeMono.ttf", 25) 
		
	def spire(self, p, angle, rate):
		'''
		p is start point, 
		angle is start angle,
		rate is scatter speed len/thita.
		'''
		r = 0
		thita = 0
		du = 2*pi/360
		self.setTextFont()
		while r<=500.0:
			posX = r * cos(thita+angle*du)
			posY = r * sin(thita+angle*du)
			pSpare = (posX+p[0],posY+p[1])
			self.text(pSpare,'test')

			r = 1 + thita*rate
			thita = thita + du

#TESTING CODE
if __name__ == '__main__':
	im = Image.new('RGBA', (1024,1024), (255,255,255))
	draw = ImageDraw.Draw(im)

	b = SpireShape(draw)
	point = (500,500)
	b.spire(point, 0, 20)
	#b.spire(point,90,0.2)

	del draw
	im.show()
	
