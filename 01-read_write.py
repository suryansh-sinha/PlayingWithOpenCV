import cv2

# Reading images
img = cv2.imread('Basics/Photos/cat_large.jpg', cv2.IMREAD_COLOR)  # Default color flag, dont need to mention.
# img = cv2.imread('Photos/cat.jpg', cv2.IMREAD_GRAYSCALE) loads image in grayscale
# img = cv2.imread('Photos/cat.jpg', cv2.IMREAD_UNCHANGED)  if image as alpha mask or rasterized images, we use this.
print(img.shape)    # height * width * channels
cv2.imshow('Cat', img)
cv2.imwrite('Basics/Photos/cat_out.jpg', img)
cv2.waitKey(0)   # Waits till infinity for a key to be pressed

# Reading videos
# VideoCapture --> we can pass in an integer to access camera devices. 0 for default camera.
# We can also pass the path of the video
# We can take feed from webcam, video file or IP address having video feed.
# capture = cv2.VideoCapture('Basics/Videos/dog.mp4')
capture = cv2.VideoCapture(1)
opened = capture.isOpened() # returns if camera is successfully read or not.

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))      # can also use capture.get(3)
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))    # can also use capture.get(4)
frame_size = (width, height)
fps = capture.get(cv2.CAP_PROP_FPS)

# writing a video, opencv provides a fourcc codec, we're gonna use that.
# codec = cv2.VideoWriter_fourcc('M','J','P','G')
codec = cv2.VideoWriter_fourcc(*'MJPG')
output = cv2.VideoWriter('Basics/webcam_cap.avi', codec, fps, frame_size)
if opened:
    while capture.isOpened():
        # Returns the frame and a boolean saying if the frame was successfully read or not
        ret, frame = capture.read()
        if ret:
            frame = cv2.putText(frame, f'{width}x{height} @ {fps} fps', (0, 30), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(255, 255, 0))
            cv2.imshow('Video', frame)
            output.write(frame)
            if(cv2.waitKey(2) == 27):   # 27 is ASCII code for escape key
                break
        else:
            print('Stream Disconnected')
            break

capture.release()
output.release()
cv2.destroyAllWindows()