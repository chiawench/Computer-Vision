from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

def imx(im, sigma):
    imgx = zeros(im.shape)
    filters.gaussian_filter(im, (sigma,sigma), (0, 1), imgx)
    return imgx


def imy(im, sigma):
    imgy = zeros(im.shape)
    filters.gaussian_filter(im,  (sigma,sigma), (1, 0), imgy)
    return imgy

def mag(im, sigma):
    # there's also gaussian_gradient_magnitude()
    mag = sqrt(imgx**2 + imgy**2)
    #imgmag = 255 - numpy.sqrt(imgx ** 2 + imgy ** 2)
    return mag

def arc(im):
    arc = zeros(im.shape)
    arc = arctan2(imgy, imgx) * 180 / pi
    return arc





im = array(Image.open('test.jpg').convert('L'))
sigma = 2


imgx=imx(im, sigma)
imshow(imgx)
imgy=imy(im, sigma)
imshow(imgy)
imgmag=mag(im, sigma)
imshow(imgmag)
arc = arc(im)
(x,y) = arc.shape
print(x)
print(y)

print(arc[:,1])

for i in range(x):
    for j in range(y):
             if arc[i,j] >= -22.5 and arc[i,j] < 22.5 :
                 arc[i, j] = 0
             elif arc[i,j] >= 22.5 and arc[i,j] < 67.5 :
                 arc[i, j] = 45
             elif arc[i, j] >= 67.5 and arc[i, j] < 112.5:
                 arc[i, j] = 90
             elif arc[i, j] >= 112.5 and arc[i, j] < 157.5:
                 arc[i, j] = 135
             elif arc[i, j] >= 157.5:
                 arc[i, j] = 180
             elif arc[i, j] <= -22.5 and arc[i, j] > -67.5:
                 arc[i, j] = -45
             elif arc[i, j] <= -67.5 and arc[i, j] > -112.5:
                 arc[i, j] = -90
             elif arc[i, j] <= -112.5 and arc[i, j] > -157.5:
                 arc[i, j] = -135
             else:
                 arc[i,j] = 180



print(arc[:,1])


