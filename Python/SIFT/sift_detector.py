import numpy as np
import math
import scipy
from scipy import ndimage
import cv2

def get_features(imagename):


    #initial sigma
    init_sigma = 1.6
    intvls = 3
    s = intvls
    k = 2**(1 / s)
    sigma = np.ones((1, s + 3))
    sigma[1] = init_sigma
    sigma[2] = init_sigma * math.sqrt(k * k - 1)

    for i in range(s,s+3):
        sigma[i] = sigma[i - 1] * k

    fx = 2
    fy = 2
    #img1 = imagename
    img1 = cv2.resize(imagename, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
    ndimage.filters.gaussian_filter(img1, math.sqrt(init_sigma *init_sigma - 1))
    min_size = min(img1.shape)
    octv = math.floor(math.log(min_size, 2) - 2)
