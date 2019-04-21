import cv2
import matplotlib as mpl
from PIL import Image
mpl.use('TkAgg')

import matplotlib.pyplot as plt


image = cv2.imread('rgb.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize = (6, 6))
plt.subplot(221),plt.imshow(img),plt.title('ORIGINAL')
plt.subplot(222),plt.imshow(img[:,:,0], cmap='gray'),plt.title('Red Channel')
plt.subplot(223),plt.imshow(img[:,:,1], cmap='gray'),plt.title('Green Channel')
plt.subplot(224),plt.imshow(img[:,:,2], cmap='gray'),plt.title('Blue Channel')
plt.savefig('./outputs/plot1')
plt.show()