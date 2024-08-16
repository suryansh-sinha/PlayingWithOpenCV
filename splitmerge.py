import cv2
import numpy as np

img = cv2.imread('Basics/Photos/park.jpg')
cv2.imshow('Boston', img)

b, g, r = cv2.split(img)
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

blue = img.copy()
blue[:, :, 1:] = 0
cv2.imshow("BLEWSS", blue)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv2.merge([b, g, r])
cv2.imshow('Merged image', merged)

cv2.waitKey(0)