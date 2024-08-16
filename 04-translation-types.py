import cv2
import numpy as np

img = cv2.imread('Photos/park.jpg', cv2.IMREAD_COLOR)
cv2.imshow('original', img)

# Using Euclidean/Isometric Transforms
# Here, we have 3 degrees of freedom, x axis, y axis, rotation.
# Translation Matrix - 2x3 Matrix in the format -
# T = [[1, 0, t_x],
#      [0, 1, t_y]]
# Here t_x, t_y are pixels we want to shift by along the x and y axes. 

matrix = np.float32([[1, 0, 100],
                     [0, 1, 100]])

translated = cv2.warpAffine(img, matrix, (img.shape[1] + 100, img.shape[0] + 100))
cv2.imshow('translated', translated)

# Using Affine Transforms
# Here, we have 6 degrees of freedom -> 2 for translation, 1 for scaling,
# 1 for scaling direction, 1 for scaling ratio, 1 for rotation.
# Here too we need a translation matrix.
# We can apply affine transformations using 3 points in image
# Source points are the points we choose in the starting image
# Destination points are points where we want to move the original points
# We can get the affine transformation matrix using getAffineTransform function.
# Then we can apply this using the warpAffine function.

cols, rows = img.shape[:2]
src_points = np.float32([[0, 0],
                         [rows-1, 0],
                         [0, cols-1]])

dst_points = np.float32([[0, 0],
                         [int(0.6*(rows-1)),0],
                         [int(0.4*(cols-1)),rows-1]])

affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matrix, (cols, rows))
cv2.imshow('affine_transformed', img_output)

cv2.waitKey(0)
cv2.destroyAllWindows()