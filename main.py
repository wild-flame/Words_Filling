from mylib import myPaste
import Image
import os, sys

im = Image.open("test_bit_3.png")
word = Image.open("baicizhan_R.png")

for x1 in range(100,1900,500):
	for y1 in range(100,1900,100):
		myPaste(x1,y1,im,word)

im.show()




