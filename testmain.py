from math import *
from mylib import *
import os, sys, Image

"""In this version you can use ARGUMENT to control this application"""

im = Image.open("./data/test_bit_2.png")
word = Image.open("./data/baicizhan_test.png")

r=1.0 #argv[0]
angle= 0.0 #argv[1]
rate = 5.0 #argv[2] , The extend of tightness
thita = 0.0 #argv[3]
du = 2*pi/360 #argv[4]

while r<=800:
	posX = r * cos(thita+angle*du)
	posY = r * sin(thita+angle*du)
	myPaste(int(posX)+1000,int(posY)+1300,im,word)
	print 'x1 ='+str(posX)+'y1 ='+str(posY)
	r = 1 + thita*rate
	thita = thita + du

im.save('test.png')

