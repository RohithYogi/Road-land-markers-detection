import cv2
import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt

image = cv2.imread('noisy.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

blur1 = cv2.GaussianBlur(image,(11,11),0)

blur2 = cv2.GaussianBlur(image,(3,3),0)

blur3 = cv2.GaussianBlur(image,(1,1),0)

plt.figure(figsize = (6, 6))
plt.subplot(221),plt.imshow(image),plt.title('ORIGINAL')
plt.subplot(222),plt.imshow(blur1),plt.title('GaussianBlur 5x5')
plt.subplot(223),plt.imshow(blur2),plt.title('GaussianBlur 3x3')
plt.subplot(224),plt.imshow(blur3),plt.title('GaussianBlur 1x1')
plt.savefig('./outputs/plot6')
plt.show()