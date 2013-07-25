import random,Image,ImageOps
from math import *

def myPaste(x1,y1,im,word):
	'''This method is used to add letter to the image'''

	'''Get the image size'''
	im_xsize, im_ysize = im.size

	'''Rotate the word image randomly'''
	word = myRotate(word)

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
				print 'flag='+str(flag)
				break
			elif (x1 + i < im_xsize) and (y1 + j < im_ysize):
				if (im_pix[x1+i,y1+j] == 0):
					flag = 0
					break		
	
	'''The paste procedure'''
	for i in range(word_xsize):
		for j in range(word_ysize):
			if flag == 1:
				im_pix[x1+i,y1+j] = (word_pix[i,j] + im_pix[x1+i,y1+j]) % 2 
	return flag
				
def myRotate(word):
	'''Rotate the image'''
	angle = random.uniform(-80,80)
	# print angle
	word = word.rotate(angle, expand = True)
	return word
	
def myConvert(im,x_new):
	'''This is used for convert the image to bit mode and resize it'''
	'''This script convert the image file to binary mode.'''
	x_size,y_size = im.size
	im = im.convert('1')
	# im = myInvert(im)
	word = im.resize((x_new,int(float(x_new)/x_size * y_size)))
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
	
def mySpirel(r,angle,rate,thita,du,im,pathname,x_new,count):
	'''
	The Spirel Method
	The im is the picture
	the pathname is where the pic are saved and it is a list
	'''
	word = Image.open(pathname[count])
	word = myConvert(word,x_new)
	while r<=800:
		posX = r * cos(thita+angle*du)
		posY = r * sin(thita+angle*du)
		flag=myPaste(int(posX)+1000,int(posY)+1000,im,word)
		r = 1 + thita*rate
		thita = thita + du
		print 'x1 ='+str(posX)+'y1 ='+str(posY)
		if flag==1:
			count = count + 1;
			word = Image.open(pathname[count])
			word = myConvert(word,x_new) #Convert the image to binary and resize it.
	return count
