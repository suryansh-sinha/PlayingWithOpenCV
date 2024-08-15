import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv2.imshow('Blank', blank)

img = cv2.imread('Photos/cats.jpg')
cv2.imshow('Cat', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
# cv2.imshow('Blur', blur)

# canny = cv2.Canny(blur, 125, 175)
# cv2.imshow('Canny Edges', canny)

# Binary Thresholding --> If pixel val below 125, set to 0, else set to 255.
ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholded', thresh)

# RETR_TREE -> to find all hierarchical contours
# RETR_EXTERNAL -> only the external contours
# RETR_LIST -> find all the contours in the image
# contour approximation method --> chain approx none does nothing
# looks at edges and returns 2 values --> contours, hierarchical representation of contours
contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found.')

# Drawing the contours on blank image
# -1 means we want to draw all the contours
cv2.drawContours(blank, contours, contourIdx=-1, color=(0, 0, 255), thickness=1)
cv2.imshow('Contours Drawn', blank)

cv2.waitKey(0)