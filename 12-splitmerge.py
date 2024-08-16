import cv2
import numpy as np

img = cv2.imread('Photos/park.jpg')
cv2.imshow('Boston', img)

blank = np.zeros(img.shape[:2], dtype=np.uint8)

b, g, r = cv2.split(img)
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])
cv2.imshow("BLEWSS", blue)
cv2.imshow("GREENS", green)
cv2.imshow("REDSSS", red)

merged = cv2.merge([b, g, r])
cv2.imshow('Merged image', merged)

cv2.waitKey(0)