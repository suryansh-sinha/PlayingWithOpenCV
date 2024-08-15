import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Photos/park.jpg')
cv2.imshow('Boston', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# BGR to Hue Saturation Value (HSV)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# BGR to LAB 
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # This shows inverted colors in OpenCV
cv2.imshow('RGB', rgb)

# Cant convert Grayscale to HSV directly.
# HSV to BGR
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('HSV-->BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv2.waitKey(0)