import cv2

img = cv2.imread('Photos/bear.jpg', cv2.IMREAD_COLOR)

# Converting image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# This is global thresholding. Over the entire image, we only use 1 threshold value that is 90.
# Take the image and convert it into a binary image.
# Pixels below 80 --> 0, above 80 --> 255.
ret, thresh = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)

# We can see some noise in the bg. We can improve our results.
blurred = cv2.blur(thresh, (10, 10))
ret, blurred = cv2.threshold(blurred, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.imshow('better thresh', blurred)
cv2.waitKey(0)