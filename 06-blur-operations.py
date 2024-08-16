import cv2
import numpy as np

# read the image
img = cv2.imread('Photos/park.jpg', cv2.IMREAD_COLOR)
rows, cols = img.shape[:2]

# Kernel blurring using filter2D()
kernel_25 = np.ones((25, 25), dtype=np.float32) / 625.0
output_kernel = cv2.filter2D(img, -1, kernel_25)

# Average blur function blurring. ksize = kernel size
output_blur = cv2.blur(img, ksize=(25, 25)) # This does the same thing as above two lines.

# Box filter. Here normalize=False matlab divide nahi kar raha woh total se.
# Sometimes used to increase the intensity of the image.
# (image, ddepth - depth of the image, kernel_size, normalize or not)
output_box = cv2.boxFilter(img, -1, (5, 5), normalize=False)    # Here, it should output white img (unnormalized)

# Gaussian Blur 
# ksize = kernel size, sigmaX = std in X direction, 
output_gaussian = cv2.GaussianBlur(img, (5, 5), sigmaX=0)

# Median Blur. Used for noise reduction in images.
# Finds the median of the pixel values in the kernel instead of the average.
output_median = cv2.medianBlur(img, ksize=5)

# Bilateral Blur. Most effective.
# Retains the edges in the image.
# d = diameter from the center pixel
# sigmaColor -> larger value means more colors in the neighbourhood are considered when blur computed.
# the higher sigmaColor, the more nearby colors combine to create a single color.
# sigmaSpace -> larger value means pixels further out from center pixel will affect blur computation.
output_bilateral = cv2.bilateralFilter(img, d=10, sigmaColor=35, sigmaSpace=35)

cv2.imshow('Kernel Blur', output_kernel)
cv2.imshow('Blur Function', output_blur)
cv2.imshow('Box Function', output_box)
cv2.imshow('Gaussian Blur', output_gaussian)
cv2.imshow('Median Blur', output_median)
cv2.imshow('Bilateral Blur', output_bilateral)
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()