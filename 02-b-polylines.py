import cv2
import numpy as np

# Poly lines are used to join multiple points in an image.

blank = np.zeros((300, 300), dtype='uint8')
cv2.imshow('Canvas', blank)

pts = np.array([[250, 5], [220, 80], [100, 100]], np.int32)
# print(pts, '\n\n')

# Reshape the points
# OpenCV expects the points in a 3D array of (number_of_vertices, 1, 2).
pts = pts.reshape((-1, 1, 2))
# print(pts, pts.shape)

# Draw this polygon
# Here boolean true or false determine if the figure is closed
cv2.polylines(blank, [pts], isClosed=True, color=(0, 255, 0), thickness=3)
cv2.imshow("Polygon", blank)


cv2.waitKey(0)