import numpy as np
import cv2

from utils import CFEVideoConf, image_resize

#cap = cv2.VideoCapture(0)
##save1_path = '/watermark.avi'    

##cap = cv2.VideoCapture(save1_path)

##save_path = 'watermark1.avi'
##frames_per_seconds = 24
##config = CFEVideoConf(cap, filepath=save_path, res='720p')
##out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)

##img_path = 'il_text.png'
img_path = './il_text.png.png'
logo = cv2.imread(img_path, -1)
watermark = cv2.resize(logo, 10)


import cv2
cap = cv2.VideoCapture('watermark.avi')
count = 0
while cap.isOpened():
    ret,frame = cap.read()

    frame_h, frame_w, frame_c = frame.shape
    overlay = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    watermark_h, watermark_w, watermark_c = logo.shape
    for i in range(0, watermark_h):
        for j in range(0, watermark_w):
            if watermark[i,j][3] != 0:
                offset = 10
                h_offset = frame_h - watermark_h - offset
                w_offset = frame_w - watermark_w - offset
                overlay[h_offset + i, w_offset+ j] = watermark[i,j]

    cv2.imshow('window-name',frame)
    cv2.imwrite("frame%d.jpg" % count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows