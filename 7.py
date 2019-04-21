import numpy as np
import random
import cv2
import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt

image = cv2.imread('gray_image.jpg')

sap = np.zeros(image.shape,np.uint8)

probability = 0.05

thres = 1 - probability

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        rdn = random.random()
        if rdn < probability:
            sap[i][j] = 0
        elif rdn > thres:
            sap[i][j] = 255
        else:
            sap[i][j] = image[i][j]

cv2.imwrite('sp_noise.jpg',sap)

median = cv2.medianBlur(sap,3)

plt.figure(figsize = (10, 6))
plt.subplot(131),plt.imshow(image),plt.title('ORIGINAL')
plt.subplot(132),plt.imshow(sap),plt.title('salt-and-pepper noise')
plt.subplot(133),plt.imshow(median),plt.title('medianBlur')

plt.savefig('./outputs/plot7')
plt.show()