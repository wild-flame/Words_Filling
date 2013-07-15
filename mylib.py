import random,Image

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
	for i in range(word_xsize):
		for j in range(word_ysize):
			if (x1 + i >= im_xsize) or (y1 + j >= im_ysize) or im_pix[x1+i,y1+j] == 0 :
				flag = 0
				break

	'''The paste procedure'''
	for i in range(word_xsize):
		for j in range(word_ysize):
			if flag == 1:
				im_pix[x1+i,y1+j] = (word_pix[i,j] + im_pix[x1+i,y1+j]) % 2
	return word_xsize, word_ysize
				
def myRotate(word):
	'''Rotate the image'''
	angle = random.uniform(-80, 80)
	print angle
	word = word.rotate(angle, expand = True)
	return word




