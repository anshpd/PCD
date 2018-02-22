import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('image1.jpg')
img = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Current Image', img1)
cv2.imshow('Grey-scale Image', img)
histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram for grey-scale image')
plt.show()

while True:
    a = cv2.waitKey(0) & 0xFF
    if a == 27: break
cv2.destroyAllWindows()