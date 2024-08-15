# Read a video and output it's reverse.
import cv2

# Creating capture source
cap = cv2.VideoCapture('Basics/Videos/dog.mp4')

# Getting video properties
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
frame_size = (width, height)

# Creating the codec
codec = cv2.VideoWriter_fourcc(*'MJPG')
output = cv2.VideoWriter('Basics/reversed.avi', codec, fps, frame_size)

print(total_frames)

# Starting at the end
frame_index = total_frames - 1
if (cap.isOpened):
    while(frame_index != 0):
        # Set the current frame position to last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        output.write(frame)
        frame_index -= 1
        
        # Printing the progress
        if(frame_index%100 == 0):
            print(frame_index)
            
output.release()
cap.release()
cv2.destroyAllWindows()