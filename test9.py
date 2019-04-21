import os
import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
import matplotlib as mpl
from PIL import Image
mpl.use('TkAgg')

import matplotlib.pyplot as plt


def read_files(path):
   s = 1
   feature_list = list()
   label_list   = list()
   num_classes = 0
   for root, dirs, files in os.walk(path):
      for d in dirs:
         num_classes += 1
         images = os.listdir(root+d)
         for image in images:
            s += 1
            label_list.append(d)
            feature_list.append(extract_feature(root+d+"/"+image))

   return np.asarray(feature_list), np.asarray(label_list)

def extract_feature(image_file):
   img = cv2.imread(image_file)
   img = cv2.resize(img, SHAPE, interpolation = cv2.INTER_CUBIC)
   img = img.flatten()
   img = img/np.mean(img)
   return img


feature_array, label_array = read_files(path)


X_train, X_test, y_train, y_test = train_test_split(feature_array, label_array, test_size=0.2, random_state=42)

right = 0
total = 0
for x, y in zip(X_test, y_test):
    x = x.reshape(1, -1)
    prediction = svm.predict(x)[0]

    if y == prediction:
        right += 1
    total += 1

accuracy = float(right)/float(total)*100
print str(accuracy) + "% accuracy"



# IplImage DstImage = cvCreateImage(cvSize(rows, cols), IPL_DEPTH_8U, 1);


# angle = ((180 / 90) % 4) * 90

# flip_horizontal_or_vertical = angle &gt; 0 ? 1 : 0
# number =abs(angle / 90);
# for i in range(0,number):
#     cvTranspose(grayImage, DstImage)       
#     cvFlip(grayImage,DstImage,flip_horizontal_or_vertical)