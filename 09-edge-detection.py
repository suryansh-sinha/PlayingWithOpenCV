import cv2
import numpy as np

img = cv2.imread('Photos/group 2.jpg')

# Canny edge detector
img_edge = cv2.Canny(img, 100, 200)

# Dilate -> Makes edges more thicker.
# Helps improve the edge boundaries.
# Higher the kernel size, higher the thickness
img_edge_dilate = cv2.dilate(img_edge, np.ones((5, 5), dtype=np.uint8))

# Erode -> Makes the edges more thinner.
img_edge_erode = cv2.erode(img_edge_dilate, np.ones((5,5), dtype=np.uint8))

cv2.imshow('img', img)
cv2.imshow('Edge', img_edge)
cv2.imshow('Dilate', img_edge_dilate)
cv2.imshow('Erode', img_edge_erode)

cv2.waitKey(0)