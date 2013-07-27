from math import *
from mylib import *
import Image, os, sys

"""FIRST STEP: GET THE INPUT ARGUMENT"""
#These are arguments which are used for the fisrt walk-through

PROBABILITY = 1# The input probability of the fisrt input.

#These are arguments which are used for the second walk-through
rate = 10.0 # The extend of tightness
du = 10*pi/360 #

im = Image.open("../data/Freedom_bit_2.png")
pathname = []
srchpath = '../image/data'

'''Get the every pathname of the data'''
for root, dirs, files in os.walk(srchpath):
	for file in files:
		pathname[len(pathname):] = [os.path.join(root, file)]

word,size,rotate_angle,position = [],[],[],[]
"""SECOND STEP: INPUT THE PIC FOR THE FISRT TIME(RANDOMLY)"""
count = 0 #count the pic
count = myRec(im,pathname,count,RESIZE_SCALE=3)
count = myRec(im,pathname,count,RESIZE_SCALE=4)
count = myRec(im,pathname,count,RESIZE_SCALE=5)

"""THIRD STEP: INPUT THE PIC FOR THE SECOND TIME(TO PUT THE PIC IN WHITE SPACE)"""
# count = mySpirel(rate,du,im,pathname,RESIZE_SCALE=6,count,rotate_angle=40,START_X,START_Y)
for posX in range(1000,1801,800):
	for posY in range(1000,3401,800):
		count = mySpirel(rate,du,im,pathname,6,count,-80,posX,posY)


"""FOURTH STEP: OUTPUT THE DATA CSV or JSON"""
im.save('test.png')
# myWrite()

