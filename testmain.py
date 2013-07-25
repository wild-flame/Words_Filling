from math import *
import Image
from mylib import *
import os, sys

im = Image.open("./data/test_bit_2.png")
word = Image.open("./data/baicizhan_test.png")

r=0
angle=0
rate = 5 # The extend of tightness
thita = 0
du = 2*pi/360
while r<=800:
	posX = r * cos(thita+angle*du)
	posY = r * sin(thita+angle*du)
	myPaste(int(posX)+1000,int(posY)+1000,im,word)
	print 'x1 ='+str(posX)+'y1 ='+str(posY)
	r = 1 + thita*rate
	thita = thita + du

im.save('test.png')

