import cv2 
import numpy as np 
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import glob

def show_images(images):
    
    plt.figure(figsize = (10, 11))
    for i in range(len(images)):
        img = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
        plt.subplot(len(images)/2, 2, i+1)
        plt.imshow(img)
        plt.xticks([])
        plt.yticks([])
    plt.tight_layout(pad = 0, h_pad = 0, w_pad = 0)
    plt.savefig('./outputs/plot8')
    plt.show()


def covert_gray(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def smoothing(gray):

    gus = cv2.GaussianBlur(gray, (3, 3), 0)
    return gus

def get_edges(gus):

    edges = cv2.Canny(gus, 300, 550)
    return edges



def region_of_interest(img, vertices):

    mask = np.zeros_like(img)   
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
  
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img,mask):
    
    lines = cv2.HoughLinesP(mask, 1, np.pi/180, 35, maxLineGap=70)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 4)


images = [cv2.imread(file,1) for file in glob.glob('roads/*.jpg')]

# show_images(images)

for i in range(len(images)):

    l = images[i].shape
    height =l[0]
    width =l[1]
    print(str(height)+" "+str(width))

    region_of_interest_vertices = [
        (0, height),
        # (width / 3, height / 3),
        (0, height / 2),
        (width, height/2),
        (width,height)
    ]
    gray = covert_gray(images[i])
    gus = smoothing(gray)
    edges = get_edges(gus)
    mask = region_of_interest(edges,np.array([region_of_interest_vertices], np.int32))
    draw_lines(images[i],mask)

show_images(images)

