import cv2

img = cv2.imread('Basics/Photos/lady.jpg', cv2.IMREAD_GRAYSCALE)

# Binary thresholding.
ret, thresh = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)  # Any pixel vales above 100, become 255.



cv2.imshow('Original', img)
cv2.imshow('Thresh', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()