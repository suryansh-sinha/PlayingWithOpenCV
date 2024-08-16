import cv2

img = cv2.imread('Photos/handwritten.png', cv2.IMREAD_GRAYSCALE)

# Sometimes global thresholding is just not able to do the job.
ret, thresh = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)

# We are going to use adaptive thresholding.
# OpenCV figures out threshold value automatically.
# Each segment of the image will have different threshold value.
# we can also use ADAPTIVE_THRESH_MEAN instead of gaussian.
# We create small filter of size 20, and use threshold in that window.
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=21, C=20)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.imshow('thresh2', thresh2)
cv2.waitKey(0)