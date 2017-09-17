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
figure()
gray()

sigma = 2


subplot(1, 5, 1)
axis('off')
imshow(im)
imgx=imx(im, sigma)
subplot(1, 5, 2)
axis('off')
imshow(imgx)
imgy=imy(im, sigma)
subplot(1, 5, 3)
axis('off')
imshow(imgy)
imgmag=mag(im, sigma)
subplot(1, 5, 4)
axis('off')
imshow(imgmag)
arc = arc(im)
subplot(1, 5, 5)
axis('off')
imshow(arc)

show()