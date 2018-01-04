from PIL import Image
from numpy import *
from pylab import *
from scipy import ndimage
import cv2
import math
#import sift_detector

img1 = cv2.imread('book.pgm')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print(img1.shape)
img2 = cv2.imread('scene.pgm')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#initial sigma
init_sigma = 1.6
intvls = 3
s = intvls
k = 2**(1 / s)
sigma = np.ones((1, s + 3))
sigma[0,0] = init_sigma
sigma[0,1] = init_sigma * math.sqrt(k * k - 1)

for i in range(s,s+3):
    sigma[0,i] = sigma[0,i - 1] * k

fx = 2
fy = 2
img1 = cv2.resize(img1, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
min_size = min(img1.shape)
octvs = math.floor(math.log(min_size,2)-2)
gauss_pyr = list()
gimg_size = np.ones((octvs,2),dtype=np.int)
gimg_size[0,0] = round(img1.shape[0])
gimg_size[0,1] = round(img1.shape[1])
print(gimg_size[0,0])
intvls = 3
s = intvls
for i in range(0, octvs-1):
    if(i !=0):
       gimg_size[i,:] = [round(gauss_pyr[i-1].shape[0]/2),round(gauss_pyr[i-1].shape[1]/2)]
    gauss_pyr.append(np.zeros((gimg_size[i,0],gimg_size[i,1],s+3)))

print(gauss_pyr[0][:,:,0].shape)
for i in range(0, octvs - 1):
    for j in range(0, s+2) :
        if( i==0 and j==0 ):
            gauss_pyr[i][:, :, j] = img1
        elif j==0:
            gauss_pyr[i][:,:,j] = cv2.resize(gauss_pyr[i-1][:,:,j], (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
        else:
            gauss_pyr[i][:, :, j] = ndimage.filters.gaussian_filter(gauss_pyr[i][:, :, j-1],sigma[0,j] )
#print(gauss_pyr[6][0][0][1])
#print(gauss_pyr[6].shape[1])
#print(gauss_pyr[6].shape[2])
#print(octv)
#figure()
#subplot(121)
#imshow(img1)
#subplot(122)
#imshow(img1)
#show()





