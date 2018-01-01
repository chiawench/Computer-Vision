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





im = array(Image.open('test.png').convert('L'))
sigma = 2


imgx=imx(im, sigma)
#imshow(imgx)
imgy=imy(im, sigma)
#imshow(imgy)
imgmag=mag(im, sigma)
#imshow(imgmag)
arc = arc(im)
(x,y) = arc.shape
print(x)
print(y)

ime = Image.fromarray(uint8(imgmag))
ime.save("mag.jpg")
nms = zeros(im.shape)

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


for i in range(1,x-1):
    for j in range(1,y-1):
        if(arc[i,j] == 0 or arc[i,j] == 180) :
            if(imgmag[i,j] >imgmag[i,j-1] and imgmag[i,j] > imgmag[i,j+1]) :
                nms[i,j] = imgmag[i,j]
            else:
                nms[i, j] = 0
        if (arc[i, j] == 45 or arc[i, j] == -135):
            if (imgmag[i, j] > imgmag[i-1, j + 1] and imgmag[i, j] > imgmag[i+1, j - 1]):
                nms[i, j] = imgmag[i,j]
            else:
                nms[i, j] = 0
        if (arc[i, j] == 90 or arc[i, j] == -90):
            if (imgmag[i, j] > imgmag[i-1, j ] and imgmag[i, j] > imgmag[i+1, j]):
                nms[i, j] = imgmag[i,j]
            else:
                nms[i, j] = 0
        if (arc[i, j] == 135 or arc[i, j] == -45):
            if (imgmag[i, j] > imgmag[i-1, j - 1] and imgmag[i, j] > imgmag[i+1, j + 1]):
                nms[i, j] = imgmag[i,j]
            else:
                nms[i, j] = 0

ime = Image.fromarray(uint8(nms))
ime.save("nms.jpg")







