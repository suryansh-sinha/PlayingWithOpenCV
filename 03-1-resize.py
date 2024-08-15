import cv2

def resizeFrame(frame, interpolation: int, scale=1.5):
    # Works with images, videos, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv2.resize(frame, dimensions, interpolation=interpolation)

# Scaling always requires interpolation which are techniques used to fill blank spaces.
# 5 types of interpolation in OpenCV - Linear, Cubic, Area, Nearest Neighbours, Sinusoidal.
# Linear is fastest, cubic is slow but gives good contrast ratio.

img = cv2.imread('Basics/Photos/park.jpg')
linearImg = resizeFrame(img, cv2.INTER_LINEAR, scale=1.5)
cubicImg = resizeFrame(img, cv2.INTER_CUBIC, scale=1.5)
areaImg = resizeFrame(img, cv2.INTER_AREA, scale=1.5)
cv2.imshow('Original Img', img)
cv2.imshow('Linearly Interpolation Rescaled Image', linearImg)
cv2.imshow('Cubic Interpolation Rescaled Image', cubicImg)
cv2.imshow('Area Interpolation Rescaled Image', areaImg)
cv2.waitKey(0)

def changeRes(width, height):
    # Only works on live video NOT on images, videos.
    capture.set(3, width)   # 3 is width.
    capture.set(4, height)  # 4 is height.

capture = cv2.VideoCapture('Videos/dog.mp4')

while True:
    # Returns the frame and a boolean saying if the frame was successfully read or not
    isTrue, frame = capture.read()
    
    frame_resized = resizeFrame(frame, scale=0.5)
    
    cv2.imshow('Video', frame)
    cv2.imshow('Video Resized', frame_resized)
    
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv2.destroyAllWindows()