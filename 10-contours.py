import cv2
import numpy as np

img = cv2.imread('Photos/birds.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# For working with contours, we need the objects we want to detect to be white.
# Take pixels below 127 to 255. Pixels above 127 to 0.
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

# contours take single channel image as input.
# all the isolated objects (white birds in our case) have a contour or a border.
# this function returns a list of contours for all the different objects in the image.
# cv2.RETR_TREE if you want all the hierarchical contours
# cv2.RETR_EXTERNAL if you want all the external contours
# cv2.RETR_LIST if you want all the contours in the image.
# cv2.CHAIN_APPROX_SIMPLE is a contour approximation method.
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # cv2.contourArea gives us the area of a contour.
    # Contours with small area may be noise values. So, we take it as 200.
    if cv2.contourArea(cnt) > 200:
        # Drawing all the contours on top of our image -
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)
        
        # We get coordinates of rectangles around each of our contours.
        # x1, y1 --> Coordinates of top left point
        # w, h --> Width of rectangle, Height of rectangle.
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2, lineType=cv2.LINE_AA)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)