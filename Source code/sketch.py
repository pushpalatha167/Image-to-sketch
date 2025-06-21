import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "your-image.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def dodge(front, back):
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')

ss = imageio.imread(img)
gray = rgb2gray(ss)
i = 255 - gray
blur = scipy.ndimage.gaussian_filter(i, sigma=15)
r = dodge(blur, gray)
cv2.imwrite("sketch_output.png", r)