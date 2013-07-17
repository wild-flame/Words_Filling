from mylib import *
import Image
import os, sys

im = Image.open("Second_2.png")
# word = Image.open("0010_oilfield.jpg")

pathname = []
srchpath = '../image/data'

for root, dirs, files in os.walk(srchpath):
	for file in files:
		pathname[len(pathname):] = [os.path.join(root, file)]
gi
'''Define the boundary to start scanning'''
R_left,R_up,R_right,R_bottom = [1200,1200,4800,8800]

count = 0 # count how many picture has been put in
x1 = R_left

while x1 < R_right:
	y1 = R_up
	print 'x1 ='+ str(x1)
	while y1 < R_bottom:
		word = Image.open(pathname[count])
		word = myConvert(word) #Convert the image to binary and resize it.
		x_step, y_step = myPaste(x1,y1,im,word)
		count = count + 1;
		y1 = y1 + y_step
		print 'y1 ='+ str(y1)
	x1 = x1 + x_step

im.save('test.png')

