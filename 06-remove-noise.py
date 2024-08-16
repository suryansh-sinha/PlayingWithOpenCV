import cv2

img = cv2.imread('Photos/cow-salt-peper.png')

k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_median_blur = cv2.medianBlur(img, k_size)   # Works best for noise removal

cv2.imshow('Original', img)
cv2.imshow('Average Blur', img_blur)
cv2.imshow('Gaussian Blur', img_gaussian_blur)
cv2.imshow('Median Blur', img_median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()