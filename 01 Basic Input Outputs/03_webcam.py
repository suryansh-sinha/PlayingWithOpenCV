import cv2

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640) # Setting Width of Image (Code 3)
cap.set(4, 480) # Setting Height of Image (Code 4)
cap.set(10, 100) # Setting brightness to 100 (Code 10 for brightness)

while True:
    success, img = cap.read()   # Success stores boolean, if frame was read successfully or not.
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break