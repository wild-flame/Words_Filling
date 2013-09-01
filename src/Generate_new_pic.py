import csv,os,sys,random,Image,ImageOps,ImageChops
from ast import literal_eval
from mylib import *

class Word:
	def __init__(self,pathname,size,position,rotate_angle,resize_scale):
		self.pathname = pathname
		self.size = literal_eval(size)
		self.position = literal_eval(position)
		self.rotate_angle = float(rotate_angle)
		self.resize_scale = float(resize_scale)

with open('input_data.csv', 'rb') as file:
	reader = csv.reader(file)
	count = 0
	All_Words = []
	for row in reader:
		print count
		if count == 0:
			count = count + 1
		else:
			All_Words.append(Word(row[0],row[1],row[2],row[3],row[4]))
			count = count + 1

count = 0
image = Image.new("RGBA", (3366, 4961), (255,255,255,255))
for word in All_Words:
	print word.pathname+','+str(word.position)+','+str(word.rotate_angle)+','+str(word.resize_scale)

	word_im = Image.open(word.pathname) 
	word_im = myRotateWhite(word_im, word.rotate_angle)
	RESIZE_SCALE = word.resize_scale
	x_size,y_size = word_im.size
	word_im = word_im.resize((int(x_size/RESIZE_SCALE),int(y_size/RESIZE_SCALE)),Image.ANTIALIAS)
	image = myComposite(image,word_im,word.position)

image.save('final.png')
