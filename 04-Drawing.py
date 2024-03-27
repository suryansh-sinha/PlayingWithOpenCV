import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    # Drawing lines on video feed
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10) # (img, startCoords, endCoords, colorOfLine, thicknessOfLine)
    img = cv2.line(img, (width, 0), (0, height), (0, 0, 255), 10)
    
    # Drawing a rectangle. Use -1 at thickness to fill the rectangle.
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)    # (img, startCoords, endCoords, colorOfRect, thicknessOfRect)
    
    # Drawing a circle. (img, centerCoords, radius, color, fill/thickness)
    img = cv2.circle(img, (width//2, height//2), 100, (0, 255, 0), 1)
    
    # Drawing text. We need to create a font first. Text starts from bottom left instead of top right.
    font = cv2.FONT_HERSHEY_SIMPLEX
    # function parameters --> (img, text input, textCoords, font, fontScale, color, fontLineThickness, TypeOfAntiAliasing)
    img = cv2.putText(img, 'SkyNet is coming!', (50, height-50), font, 1, (0, 0, 0), 3, cv2.LINE_AA)
    
    cv2.imshow("Video Capture", img)
    
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()