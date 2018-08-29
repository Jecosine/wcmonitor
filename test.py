import cv2
from PIL import Image

cap = cv2.VideoCapture(0)
count = 0
size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
writer = cv2.VideoWriter("a.avi",cv2.cv.CV_FOURCC("M","J","P","G"),20,(640,480))
while True:
    if count >= 100:
        break
    _,frame = cap.read()
    #frame = cv2.flip(frame,1)
    writer.write(frame)
    count += 1
cap.release()
writer.release()
