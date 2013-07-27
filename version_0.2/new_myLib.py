def myPaste(x1,y1,im,word,angle):

	im_xsize, im_ysize = im.size # Get the image size
	word = myRotate(word,angle)
	word_xsize, word_ysize = word.size # Get the word size
	im_pix = im.load()
	word_pix = word.load()
	
	flag=1
	'''Detect if it is able to paste'''
	'''flag == 0 if it is not able to paste'''
	for i in range(word_xsize):
		for j in range(word_ysize):
			if (x1 + i) >= im_xsize or (y1 + j) >= im_ysize: # The word has been out of the image
				flag = 0
				break	
			elif (x1 + i) < im_xsize and (y1 + j) < im_ysize: # The word is in the image but not in the right area.
				if (im_pix[x1+i,y1+j] == 0 and word_pix[i,j] == 1:
					flag = 0
					break

	'''The paste procedure'''
	for i in range(word_xsize):
		for j in range(word_ysize):
			if flag == 1:
				im_pix[x1+i,y1+j] = (word_pix[i,j] + im_pix[x1+i,y1+j]) % 2 
	return flag, word_xsize, word_ysize

def myRotate(word, angle):
	'''Rotate the image'''
	# print angle
	word = word.rotate(angle, expand = True)
	return word

def mySpirel(rate,du,im,pathname,new,count):
	'''
	The Spirel Method
	The im is the picture
	the pathname is where the pic are saved and it is a list
	'''
	r=0
	angle=0
	thita=0
	START_X = 1000
	START_Y = 1000
	R_MAX = 800

	word = Image.open(pathname[count])
	word = myConvert(word,new)
	while r<= R_MAX:
		posX = r * cos(thita+angle*du)
		posY = r * sin(thita+angle*du)
		flag, x_step, y_step =myPaste(int(posX)+START_X,int(posY)+START_Y,im,word)
		r = 1 + thita*rate
		thita = thita + du
		if flag==1:
			print 'x1 ='+str(posX)+'y1 ='+str(posY)
			print 'count ='+str(count)
			count = count + 1;
			word = Image.open(pathname[count])
			word = myConvert(word,new) #Convert the image to binary and resize it.
	return count

def myRec(im,pathname,probability,count):
	# probability
	R_left,R_up,R_right,R_bottom = [0,0,2000,2000]
	x1 = R_left
	word = Image.open(pathname[count])
	word = myConvert(word,new)
	while x1 < R_right:
		y1 = R_up
		while y1 < R_bottom:
			word = Image.open(pathname[count])
			flag, x_step, y_step = myPaste(x1,y1,im,word,angle)
			y1 = y1 + y_step
			if flag ==1:
				print 'x1 ='+str(posX)+'y1 ='+str(posY)
				print 'count ='+str(count)
				count = count + 1;
				word = Image.open(pathname[count])
				word = myConvert(word,new) #Convert the image to binary and resize it.
		x1 = x1 + x_step
	return count

def myWrite(word,size,angle,position):
	'''This method write the data into csv or json format'''
	pass