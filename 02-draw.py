import cv2
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv2.imshow('Blank Image', blank)

# 1. Paint image a certain color
blank[:] = 0, 25, 35    # B G R

# 2. Draw a rectangle using top left corner and bottom right corner coordinates.
# To fill the rectangle, thickness=cv2.FILLED or -1
cv2.rectangle(blank, (0, 0), (250, 250), (255, 0, 0), thickness=2)

# 3. Draw a circle
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)

# 4. Draw a line
# 2 types of lines in opencv - anti-aliased lines, aliased lines.
# Aliased lines have support pixels which are similiarly colored so that the line looks connected properly.
cv2.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), 4, cv2.LINE_4)
cv2.line(blank, (blank.shape[1]//2, blank.shape[0]//2), (blank.shape[1], blank.shape[0]), (0, 0, 255), 4, cv2.LINE_AA)

# 5. Arrowed line
cv2.arrowedLine(blank, (400, 400), (400, 500), (255, 255, 40), thickness=1, tipLength=0.3)

# 6. Write text on image
cv2.putText(blank, "Hello", (225, 225), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0, 225, 225), thickness=2)

cv2.imshow('Canvas', blank)
cv2.waitKey(0)