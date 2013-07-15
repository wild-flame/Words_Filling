from mylib import *
import Image
import os, sys

im = Image.open("test_zhan_6.png")
word = Image.open("baicizhan_10.png")

R_left,R_up,R_right,R_bottom = [0,0,2000,2000]

x1 = R_left
while x1 < R_right:
	y1 = R_up
	print 'x1 ='+ str(x1)
	while y1 < R_bottom:
		x_step, y_step = myPaste(x1,y1,im,word)
		y1 = y1 + y_step
		print 'y1 ='+ str(y1)
	x1 = x1 + x_step

im.save('test.png')


