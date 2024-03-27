### Image Fundamentals and Manipulation
import cv2
import numpy as np
import random

random.seed(42)

# Images in OpenCV are read as Blue, Green Red instead of standard RGB.
img = cv2.imread('resources/lena.png', -1)

# print(type(img))    # Images are represented as numpy arrays.
# print(img.shape)    # 512 rows, 512 columns, 3 channels. HWC.
# print(img[0])

# Let's replace the first 100 pixel rows by random noise.
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] # Setting pixels to random values.

# Let's copy a part of the image and place it somewhere else
# img2 = img --> This makes a reference copy of the image. Any changes made to img2 will also affect img.
img2 = img.copy()   # This makes a copy of the image, changes made to img2 will not reflect in img. From ndarray class.
tag = img[300:400, 200:400]
img2[200:300, 200:400] = tag
        
cv2.imshow("Unedited Image", img)
cv2.imshow("Edited Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()