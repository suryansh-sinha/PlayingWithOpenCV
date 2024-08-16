import cv2
import numpy as np

blank = np.zeros((400, 400), np.uint8)

rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)

cv2.imshow("rectangle", rectangle)
cv2.imshow("circle", circle)

# Bitwise AND --> Intersection of images (Only the common regions) displayed
andImg = cv2.bitwise_and(rectangle, circle)
cv2.imshow('andImg', andImg)

# Bitwise OR --> Union of images (The common region of both images) displayed
orImg = cv2.bitwise_or(rectangle, circle)
cv2.imshow('orImg', orImg)

# Bitwise XOR --> Non intersecting regions of the image.
xorImg = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('xorImg', xorImg)

# Bitwise NOT --> Inverts the image
notImg = cv2.bitwise_not(circle)
cv2.imshow('notImg', notImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
