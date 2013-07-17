from mylib import *
import Image
import os, sys

im = Image.open("Freedom_bit_2.png")
word = Image.open("0010_oilfield.jpg")

word = myConvert(word)

R_left,R_up,R_right,R_bottom = [600,600,2400,4400]

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

