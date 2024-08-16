import cv2
import numpy as np

# Height, Width, Color Channels
img = cv2.imread('Photos/park.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Boston', img)

# Warp Affine always requires a 2x3 matrix.
# warpAffine(source_img, translation matrix, size_of_op_img, output_img,
#            interpolation, extrapolation_method, value to be used in case of constant border)
# Image Translation -->
# We need to create a translation matrix for this -
# T = [[1, 0, t_x],
#      [0, 1, t_y]]
# Here t_x, t_y are pixels we want to shift by along the x and y axes.
# -x --> left, -y --> up
# +x --> right, +y --> down
# We apply the translation using the warpAffine function.
def translate(img, x, y):
    transMat = np.float32([[1, 0, x],
                           [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, 100)
cv2.imshow('Moved', translated)

# Image Rotation
# To rotate an image, we again need a rotation matrix following a specific format.
# Since the format is hard to learn, we have a function to get the rotation matrix.
# rotMat = cv2.getRotationMatrix2D(center, angle, scale)
# Takes parameters - center point about which to rotate, angle (in degrees) by which to rotate, scaling if required.
# If angle is +ve, counter-clockwise rotation, else clockwise.
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, scale=1.0)
    dimensions = (width, height)
    
    return cv2.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 30)
cv2.imshow("Rotated", rotated)

# Resizing an Image
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized", resized)

# Flip an image
# Takes image, flip code
# 0 --> Vertical flip
# 1 --> Horizontal flip
# -1 --> Both horizontal and vertical flip
flip = cv2.flip(img, -1)
cv2.imshow("Flipped", flip)

cv2.waitKey()
