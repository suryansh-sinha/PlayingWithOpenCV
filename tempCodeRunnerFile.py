import cv2

def rescaleFrame(frame, interpolation: int, scale=1.50):
    # Works with images, videos, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv2.resize(frame, dimensions, interpolation=interpolation)

img = cv2.imread('Photos/park.jpg')
linearImg = rescaleFrame(img, cv2.INTER_LINEAR, scale=1.5)
cubicImg = rescaleFrame(img, cv2.INTER_CUBIC, scale=1.5)
areaImg = rescaleFrame(img, cv2.INTER_AREA, scale=1.5)
cv2.imshow('Original Img', img)
cv2.imshow('Linearly Interpolation Rescaled Image', linearImg)
cv2.imshow('Cubic Interpolation Rescaled Image', cubicImg)
cv2.imshow('Area Interpolation Rescaled Image', areaImg)
cv2.waitKey(0)