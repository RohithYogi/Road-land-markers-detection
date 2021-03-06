import cv2
import matplotlib as mpl
from PIL import Image
mpl.use('TkAgg')

import matplotlib.pyplot as plt

img = Image.open('rgb.jpg')
image = cv2.imread('rgb.jpg')

# Convert BGR to LAB
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

plt.subplot(121),plt.imshow(img),plt.title('ORIGINAL')
plt.subplot(122),plt.imshow(lab,'gray'),plt.title('L*a*b plot')
plt.savefig('./outputs/plot3')
plt.show()