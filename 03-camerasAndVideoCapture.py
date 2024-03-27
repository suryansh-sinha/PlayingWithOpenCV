### Cameras and Video Capture
import cv2
import numpy as np

cap = cv2.VideoCapture(0)   # number of webcam/video device which you want to access.

# Infinite loop.
while True:
    ret, frame = cap.read() # ret (boolean) tells you if capture worked properly. frame is the image frame.
    width = int(cap.get(3)) # 3 gives width property of frame.
    height = int(cap.get(4)) # 4 gives height property of frame.
    
    # Splitting the frame into 3 channels of shape [height/2, width/2].
    B, G, R = cv2.split(cv2.resize(frame, (0, 0), fx=0.5, fy=0.5))
    # Creating an empty frame having same shape as above channels. [height, width].
    small_black_frame = cv2.resize(np.zeros(frame.shape[:2], dtype=np.uint8), (0, 0), fx=0.5, fy=0.5)
    # merge function used to merge 3 different channels into a single image.
    B = cv2.merge((B, small_black_frame, small_black_frame))    # Blue, 0, 0 --> Blue channel only
    G = cv2.merge((small_black_frame, G, small_black_frame))    # 0, Green, 0 --> Green channel only
    R = cv2.merge((small_black_frame, small_black_frame, R))    # 0, 0, Red --> Red channel only
    
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)   # Resizing the video frame to become 1/4th. Image with all channels.
    
    canvas = np.zeros(frame.shape, np.uint8) # Create a black frame to display all 4 outputs.
    canvas[:height//2, :width//2] = B  # Placing the blue frame on the top left.
    canvas[:height//2, width//2:] = G  # Placing the green frame on the top right.
    canvas[height//2:, :width//2] = R  # Placing the red frame on the bottom left.
    canvas[height//2:, width//2:] = smaller_frame # Placing the smaller frame on the bottom right.
    
    cv2.imshow("Video Feed", canvas)
    
    # If we press a key within 1 millisecond, the function returns the ascii value of the key that we pressed.
    # It then checks if this is equal to q, breaks the loop if true.
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()   # Releases the video resource.
cv2.destroyAllWindows()