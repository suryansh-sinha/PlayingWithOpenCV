import cv2
import numpy as np

# Creating the callback function
def onClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1, cv2.LINE_AA)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('image', img)
        
img = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.imshow('image', img)

# Creating an empty list to track clicked points.
points = []

# Binding the window with the function
cv2.setMouseCallback('image', onClick)

cv2.waitKey(0)
cv2.destroyAllWindows()