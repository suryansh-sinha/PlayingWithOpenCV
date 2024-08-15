import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# event -> event taking place when we click our mouse
# x, y -> coordinates where the mouse is clicked
# flags, params
# WINDOW NAME SHOULD BE THE SAME EVERYWHERE
def click_event(event, x, y, flags, params):
    # Print the coordinates on left click.
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'({x}, {y})')
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = f'({x}, {y})'
        cv2.putText(img, strXY, (x, y), font, 0.33, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow('image', img)
        
    # Print the BGR values on right click.
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = f'({blue}, {green}, {red})'
        cv2.putText(img, strXY, (x, y), font, 0.33, (255, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow('image', img)
    
# Creating image
img = cv2.imread('Basics/Photos/cats.jpg', cv2.IMREAD_COLOR)
cv2.imshow('image', img)

# Binding the window with the event.
cv2.setMouseCallback('image', click_event)

# Exit the program.
cv2.waitKey(0)
cv2.destroyAllWindows()