import cv2
import numpy as np

# Poly lines are used to join multiple points in an image.
blank = np.zeros((300, 300, 3), dtype='uint8')
cv2.imshow('Canvas', blank)

pts = np.array([[100, 100], [150, 80], [200, 100]], np.int32)
# print(pts, '\n\n')

# Reshape the points
# OpenCV expects the points in a 3D array of (number_of_vertices, 1, 2).
pts = pts.reshape((-1, 1, 2))
print(pts, '\n', pts.shape)

# Draw this polygon
# Here boolean true or false determine if the figure is closed
cv2.polylines(blank, [pts], isClosed=True, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
cv2.imshow("Polygon", blank)

cv2.waitKey(0)
cv2.destroyAllWindows()