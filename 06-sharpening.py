import cv2
import numpy as np

img = cv2.imread('Photos/park.jpg', cv2.IMREAD_COLOR)

# We can sharpen an image by using image arithmetics.
# We subtract blurred image from original image such that the output is 1.
# 1.5 - 0.5 = 1; 3.5 - 2.5 = 1; 7.5 - 6.5 = 1

# Gaussian kernel for sharpening
gaussianImg = cv2.GaussianBlur(img, (7,7), 2)

# Sharpening using addWeighted()
# img1, alpha, img2, beta, gamma
# alpha, beta are weights by which respective imgs are multiplied before addition.
# gamma is used to increase the intensity.
# addWeighted = img1 * alpha + img2 * beta + gamma
sharpened1 = cv2.addWeighted(img, 1.5, gaussianImg, -0.5, 0)
sharpened2 = cv2.addWeighted(img, 3.5, gaussianImg, -2.5, 0)
sharpened3 = cv2.addWeighted(img, 7.5, gaussianImg, -6.5, 0)

# showing the images
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image 1', sharpened1)
cv2.imshow('Sharpened Image 2', sharpened2)
cv2.imshow('Sharpened Image 3', sharpened3)
cv2.waitKey(0)
cv2.destroyAllWindows()