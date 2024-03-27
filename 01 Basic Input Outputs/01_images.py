import cv2

# Reading and Displaying Images
img = cv2.imread('resources/lena.jpg')
cv2.imshow("Lena Image", img)
cv2.waitKey(0)