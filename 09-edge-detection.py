import cv2

img = cv2.imread('Photos/group 2.jpg')

# Canny edge detector
img_edge = cv2.Canny(img, 80, 200)

cv2.imshow('img', img)
cv2.imshow('Edge', img_edge)

cv2.waitKey(0)