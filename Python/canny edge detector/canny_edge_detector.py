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






im = array(Image.open('test.jpg').convert('L'))
figure()
gray()

sigma = 2


subplot(1, 4, 1)
axis('off')
imshow(im)
imgx=imx(im, sigma)
subplot(1, 4, 2)
axis('off')
imshow(imgx)
imgy=imy(im, sigma)
subplot(1, 4, 3)
axis('off')
imshow(imgy)
imgmag=mag(im, sigma)
subplot(1, 4, 4)
axis('off')
imshow(imgmag)


show()