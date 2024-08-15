import cv2
import numpy as np

# Creating mouse callback function
def draw_circle(event, x, y, flags, param):
    print("Event: ", event)
    if(event == cv2.EVENT_LBUTTONDOWN):
        cv2.circle(img, (x,y), 10, (0, 255, 0), 3)
        
# Creating a blank image, a window and binding the function to the window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) == ord('q'):
        break
    
cv2.destroyAllWindows()