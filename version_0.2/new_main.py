from math import *
from mylib import *

import Image, os

"""FIRST STEP: GET THE INPUT ARGUMENT"""
#These are arguments which are used for the fisrt walk-through

PROBABILITY = 1# The input probability of the fisrt input.

#These are arguments which are used for the second walk-through
r=0 #The start radius.
angle=0 #argv[1]
rate = 5 #argv[2] , The extend of tightness
thita = 0 #argv[3]
du = 2*pi/360 #argv[4]

im = Image.open("../data/Freedom_bit_2.png")
pathname = []
srchpath = '../image/data'

'''Get the every pathname of the data'''
for root, dirs, files in os.walk(srchpath):
	for file in files:
		pathname[len(pathname):] = [os.path.join(root, file)]

word,size,angle,position = [],[],[],[]
"""SECOND STEP: INPUT THE PIC FOR THE FISRT TIME(RANDOMLY)"""
count = 0 #count the pic
count = myRec(im,pathname,PROBABILITY,count,5)

"""THIRD STEP: INPUT THE PIC FOR THE SECOND TIME(TO PUT THE PIC IN WHITE SPACE)"""

"""FOURTH STEP: OUTPUT THE DATA CSV or JSON"""
im.save('test.png')
# myWrite()

