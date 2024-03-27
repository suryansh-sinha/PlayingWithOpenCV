import cv2

# Reading and Displaying Images
img = cv2.imread('resources/lena.png', 0)

# -1, cv2.IMREAD_COLOR: Loads a color image. Any transparency of image will be neglected. It's the default flag
# 0, cv2.IMREAD_GRAYSCALE: Loads a the image in grayscale mode.
# 1, cv2.IMREAD_UNCHANGED: Loads image as such including alpha channels.

# Resizing the image
# img2 = cv2.resize(img, (400, 400))    Here it's the dimensions of the image we mentioned.
img2 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # Scales the image by 0.5 on both x and y axis.

# Rotating the image
img3 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # There are a load of options available. Check in documentation.

# Writing the image
cv2.imwrite('lena_rotated.png',img3)

cv2.imshow("Lena Image", img)
cv2.imshow("Lena Resized", img2)
cv2.imshow("Lena Rotated", img3)
cv2.waitKey(0)  # Waits upto n milliseconds for a key to be pressed else move on. 0 means infinite wait.
cv2.destroyAllWindows()