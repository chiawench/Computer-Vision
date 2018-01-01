from PIL import Image
from numpy import *
from pylab import *
from scipy import ndimage
import cv2
import math
#import sift_detector

img1 = cv2.imread('book.pgm')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#print(img1.shape)
img2 = cv2.imread('scene.pgm')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


fx = 2
fy = 2
img1 = cv2.resize(img1, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
min_size = min(img1.shape)
octv = math.floor(math.log(min_size,2)-2)
print(octv)
#figure()
#subplot(121)
#imshow(img1)
#subplot(122)
#imshow(img1)
#show()





