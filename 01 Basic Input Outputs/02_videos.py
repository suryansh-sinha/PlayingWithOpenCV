import cv2

# Reading and displaying videos.
cap = cv2.VideoCapture("resources/vtest.avi")
while True:
    success, img = cap.read()   # Success stores boolean, if frame was read successfully or not.
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break