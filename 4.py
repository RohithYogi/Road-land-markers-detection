import cv2
import matplotlib as mpl
from PIL import Image
mpl.use('TkAgg')

import matplotlib.pyplot as plt

img = Image.open('rgb.jpg')
image = cv2.imread('rgb.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(121),plt.imshow(img),plt.title('ORIGINAL')
plt.subplot(122),plt.imshow(gray,'gray'),plt.title('Grayscale plot')
plt.savefig('./outputs/plot4')
plt.show()