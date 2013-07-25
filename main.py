from math import *
import Image
from mylib import *
import os, sys

im = Image.open("./data/test_bit_2.png")

pathname = []
srchpath = '../image/data'

for root, dirs, files in os.walk(srchpath):
	for file in files:
		pathname[len(pathname):] = [os.path.join(root, file)]

count = 0 # count how many picture has been put in

'''To change the picture'''
r=0
angle=0
rate = 10 # The extend of tightness
thita = 0
du = 40*pi/360

count=0
#count=mySpirel(r,angle,rate,thita,du,im,pathname,250,count)
#count=mySpirel(r,angle,2,thita,40*pi/360,im,pathname,235,count)
#count=mySpirel(r,angle,10,thita,20*pi/360,im,pathname,220,count)
#count=mySpirel(r,angle,10,thita,20*pi/360,im,pathname,210,count)
count=mySpirel(r,angle,1,thita,2*pi/360,im,pathname,200,count)

im.save('test.png')

