import cv2
import numpy as np

img = cv2.imread("Photos/park.jpg")
cv2.imshow('Park', img)

# 1. Converting image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# 2. Blur an img -> can be used to reduce some noise
# Kernel size has to be odd number. Bigger the kernel, more the blur.
blur = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

# 3. Edge Cascades
# We're gonna use the canny edge detector.
# Can pass in a blurred image to reduce the edges compared to original.
canny = cv2.Canny(blur, 125, 175)    # image and 2 threshold values
cv2.imshow('Edges', canny)

# 4. Dilating the image using a structuring element (we're gonna use edges as element)
dilated = cv2.dilate(canny, (7, 7), iterations=3)
cv2.imshow('Dilated', dilated)

# 5. Eroding
# We can erode the dilated image to get the original image back
eroded = cv2.erode(dilated, (7, 7), iterations=3)
cv2.imshow('Eroded', eroded)

# 6. Resize
# Resizes to 500, 500 ignoring the aspect ratio.
# INTER_AREA is used to downscale the image
# To upscale the image, use INTER_LINEAR or INTER_CUBIC (slow but high quality)
resized = cv2.resize(img, (500, 500), cv2.INTER_AREA)
cv2.imshow('Resized', resized)

# Cropping an image
crop = img[50:200, 200:400]
cv2.imshow('Cropped', crop)

cv2.waitKey(0)  