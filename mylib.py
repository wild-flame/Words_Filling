import random,Image,ImageOps
from math import *

def myPaste(x1,y1,im,word, rotate_angle):
	'''This method is used to add letter to the image'''

	'''Get the image size'''
	im_xsize, im_ysize = im.size

	'''Rotate the word image randomly'''
	word = myRotate(word, rotate_angle)

	'''Get the word image size'''
	word_xsize, word_ysize = word.size
	
	'''Get every pixel of the picture'''
	im_pix = im.load()
	word_pix = word.load()
	
	'''Detection if it is able to paste'''
	flag = 1
	print 'im_xsize='+str(im_xsize)+'im_ysize'+str(im_ysize)
	print 'word_xsize='+str(word_xsize)+'word_ysize='+str(word_ysize)

	for i in range(int(word_xsize)):
		for j in range(int(word_ysize)):
			# print x1+i,y1+j
			if (x1 + i >= im_xsize) or (y1 + j >= im_ysize):
				flag = 0
				# print 'flag='+str(flag)
				break
			elif (x1 + i < im_xsize) and (y1 + j < im_ysize):
				if (im_pix[x1+i,y1+j] == 0) and (word_pix[i,j] == 1):
					flag = 0
					break
	
	'''The paste procedure'''
	for i in range(word_xsize):
		for j in range(word_ysize):
			if flag == 1:
				im_pix[x1+i,y1+j] = ( word_pix[i,j] + im_pix[x1+i,y1+j] ) % 2 
	return flag, word_xsize, word_ysize
				
def myRotate(word, rotate_angle):
	'''Rotate the image'''
	# print angle
	word = word.rotate(rotate_angle, expand = True)
	return word
	
def myConvert(im,RESIZE_SCALE):
	'''This is used for convert the image to bit mode and resize it'''
	'''This script convert the image file to binary mode.'''
	x_size,y_size = im.size
	im = im.convert('1')
	im = myInvert(im)
	word = im.resize((int(x_size/RESIZE_SCALE),int(y_size/RESIZE_SCALE)))
	return word

def myInvert(im):
	x_size,y_size = im.size 
	im_pix = im.load()
	for i in range(x_size):
		for j in range(y_size):
			if im_pix[i,j] == 0:
				im_pix[i,j] = 1
			else:
				im_pix[i,j] = 0
	return im
	
def mySpirel(rate,du,im,pathname,RESIZE_SCALE,count,rotate_angle,START_X,START_Y):
	'''
	The Spirel Method
	The im is the picture
	the pathname is where the pic are saved and it is a list
	'''
	r=0
	angle=0
	thita=0
	R_MAX = 800

	word = Image.open(pathname[count])
	word = myConvert(word,RESIZE_SCALE)
	while r<= R_MAX:
		posX = r * cos(thita+angle*du)
		posY = r * sin(thita+angle*du)
		flag, x_step, y_step =myPaste(int(posX)+START_X,int(posY)+START_Y,im,word, rotate_angle)
		r = 1 + thita*rate
		thita = thita + du
		if flag==1:
			print 'x1 ='+str(posX)+'y1 ='+str(posY)
			print 'count ='+str(count)
			count = count + 1;
			word = Image.open(pathname[count])
			word = myConvert(word,RESIZE_SCALE) #Convert the image to binary and resize it.
	return count

def myRec(im,pathname,count,RESIZE_SCALE):
	R_left,R_up,R_right,R_bottom = [500,900,2300,4400]
	x1 = R_left
	word = Image.open(pathname[count])
	word = myConvert(word,RESIZE_SCALE)
	while x1 < R_right:
		y1 = R_up
		while y1 < R_bottom:
			rotate_angle = random.uniform(-80,80)
			flag, x_step, y_step = myPaste(x1,y1,im,word,rotate_angle)
			y1 = y1 + y_step
			print 'x1 ='+str(x1)+'y1 ='+str(y1)
			if flag ==1:	
				print 'count ='+str(count)
				count = count + 1;
				word = Image.open(pathname[count])
				word = myConvert(word,RESIZE_SCALE) #Convert the image to binary and resize it.
		x1 = x1 + x_step
	return count

