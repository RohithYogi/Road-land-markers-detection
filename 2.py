import cv2
import matplotlib as mpl
from PIL import Image
mpl.use('TkAgg')

import matplotlib.pyplot as plt

image = Image.open('rgb.jpg')

print(image.size)

width, height = image.size

# # Convert BGR to HSV
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# hsl = cv2.cvtColor(image, cv2.COLOR_BGR2HLS) # equal to HSL


H = Image.new("RGB", (width, height), "white")
hpixels = H.load()

S = Image.new("RGB", (width, height), "white")
spixels = S.load()

V = Image.new("RGB", (width, height), "white")
vpixels = V.load()

L = Image.new("RGB", (width, height), "white")
lpixels = L.load()

HSV = Image.new("RGB", (width, height), "white")
hsv_pixels = HSV.load()

HSL = Image.new("RGB", (width, height), "white")
hsl_pixels = HSL.load()

# Transform to Hue
for i in range(width):
	for j in range(height):
	  
		 pixel = image.getpixel((i, j))

		 red =   pixel[0]
		 green = pixel[1]
		 blue =  pixel[2]

		 var = max(red,green,blue)

		 light = (max(red,green,blue) + min(red,green,blue))/2

		 
		 if(var!=0):
		 	sat = (var - min(red,green,blue))/var
		 else:
		 	sat = 0

		 if(var == min(red,green,blue)):
		 	hue=0
		 elif(var==red):
		 	hue = (60*(green - blue))/(var - min(red,green,blue))
		 elif(var==green):
		 	hue = (120 + 60*(blue - red))/(var - min(red,green,blue))
		 elif(var==blue):
		 	hue = (240 + 60*(red - green))/(var - min(red,green,blue))

		 if(hue<0):
		 	hue=hue+360

		 hue=hue/2
		 sat = 255 * sat

		 # print(str(var) + " " + str(sat) +" " + str(hue))
		 hpixels[i, j] = (int(hue), int(hue), int(hue))
		 spixels[i, j] = (int(sat), int(sat), int(sat))
		 vpixels[i, j] = (int(var), int(var), int(var))
		 lpixels[i, j] = (int(light), int(light), int(light))
		 
		 hsv_pixels[i, j] = (int(hue), int(sat), int(var))
		 hsl_pixels[i, j] = (int(hue), int(sat), int(light))


plt.figure(figsize = (6, 6))
plt.subplot(221),plt.imshow(image),plt.title('ORIGINAL')
plt.subplot(222),plt.imshow(H),plt.title('Hue Channel')
plt.subplot(223),plt.imshow(S),plt.title('Saturation Channel')
plt.subplot(224),plt.imshow(V),plt.title('Varience Channel')
plt.savefig('./outputs/plot2')
plt.show()

plt.figure(figsize = (6, 6))
plt.subplot(221),plt.imshow(image),plt.title('ORIGINAL')
plt.subplot(222),plt.imshow(L),plt.title('Lightness Channel')
plt.subplot(223),plt.imshow(HSL),plt.title('HSL Channel')
plt.subplot(224),plt.imshow(HSV),plt.title('HSV Channel')

plt.savefig('./outputs/plot2-2')
plt.show()

# image = cv2.imread('rgb.jpg')
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# plt.figure(figsize = (3, 3))
# plt.subplot(111),plt.imshow(hsv),plt.title('HSV Channel')
# plt.savefig('./outputs/plot2-3')
# plt.show()




# h, s, v = cv2.split(hsv)

# cv2.imshow('H', h)

# # Blue
# cv2.imshow('S', s)
# # Green
# cv2.imshow('V', v)
