import cv2
import numpy as np

img = cv2.imread('Photos/park.jpg', cv2.IMREAD_COLOR)

kernel_identity = np.array([[0, 0, 0],
                            [0, 1, 0],
                            [0, 0, 0]], dtype=np.int32)
kernel_3x3 = np.ones((3,3), dtype=np.int32) / 9.0   # dividing by total so that output is normalized.
kernel_11x11 = np.ones((11,11), dtype=np.int32) / 121.0

# horizontal blur (motion blur) ahh kernel
size = 15
kernel_horizontal = np.zeros((size, size))
kernel_horizontal[int(size-1) // 2, :] = np.ones(size)
kernel_horizontal /= 15 # Dividing to normalize outputs

# Applying the filters
# ddepth = depth of the input image. -1 takes this automatically.
op1 = cv2.filter2D(img, ddepth=-1, kernel=kernel_identity)
op2 = cv2.filter2D(img, -1, kernel_3x3)
op3 = cv2.filter2D(img, -1, kernel_11x11)
op4 = cv2.filter2D(img, -1, kernel_horizontal)

# Displaying output
cv2.imshow('op1', op1)
cv2.imshow('op2', op2)
cv2.imshow('op3', op3)
cv2.imshow('op4', op4)
cv2.waitKey(0)
cv2.destroyAllWindows()