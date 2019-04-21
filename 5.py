import cv2
import math
import matplotlib as mpl
from PIL import Image
mpl.use('TkAgg')

import matplotlib.pyplot as plt

image = Image.open('gray_image.jpg')

print(image.size)

width, height = image.size

X = Image.new("RGB", (width, height), "white")
xpixels = X.load()
mean=0
var=0

for i in range(width):
	for j in range(height):
	  
		 pixel = image.getpixel((i, j))

		 mean = mean + pixel

mean= mean / (width*height)


for i in range(width):
	for j in range(height):
	  
		 pixel = image.getpixel((i, j))

		 var = var + (pixel - mean)**2


var= var / (width*height)

print(str(mean)+" "+str(var)+" "+str(math.sqrt(var)))

for i in range(width):
	for j in range(height):
		
		 pixel = image.getpixel((i, j))

		 r =(pixel - mean) / math.sqrt(var)

		 # print(str(r)+" ")

		 xpixels[i,j]=(int(abs(r*255)),int(abs(r*255)),int(abs(r*255)))
 		
# Load image as gray scale image
image = cv2.imread('rgb.jpg',0)
equ = cv2.equalizeHist(image)
plt.figure(figsize = (10, 6))
plt.subplot(131),plt.imshow(image,'gray'),plt.title('ORIGINAL')
plt.subplot(132),plt.imshow(equ,'gray'),plt.title('Histogram Equalization')
plt.subplot(133),plt.imshow(X),plt.title('Whitening the image')
plt.savefig('./outputs/plot5')
plt.show()