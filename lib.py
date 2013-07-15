def myPaste(x1,y1,im,word):
	'''This method is used to add letter to the image'''

	'''Get the image size'''
	im_xsize, im_ysize = im.size

	'''Get the word image size'''
	word_xsize, word_ysize = word.size

	'''Get every pixel of the picture'''
	im_pix = im.load()
	word_pix = word.load()
	
	for i in range(word_xsize):
		for j in range(word_ysize):
			if (x1 + i < im_xsize) and (y1 + j < im_ysize):
				im_pix[x1+i,y1+j] = (word_pix[i,j] + im_pix[x1+i,y1+j]) % 2
				

