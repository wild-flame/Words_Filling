import ImageFile

fp = open("lena_gray_512.tif", "rb")

p = ImageFile.Parser()

while 1:
	s = fp.read()
	if not s:
		break
	p.feed(s)

im = p.close()

im.save("copy.jpg")
