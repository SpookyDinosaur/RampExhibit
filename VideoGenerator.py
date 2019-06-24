import numpy as np
import cv2
import re  
import sys
import os

from utils import CFEVideoConf, image_resize

user_input = input("Enter the path of your file: ")

print(user_input)

img_path = './pil_text.png'
logo = cv2.imread(img_path, -1)
logo = cv2.cvtColor(logo, cv2.COLOR_BGR2BGRA)

cap = cv2.VideoCapture(user_input)
count = 0
while cap.isOpened():
    ret,frame = cap.read()

    try:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    except:
        print("Video Over")
        break

    rows,cols,channels = frame.shape

    watermark_h, watermark_w, watermark_c = logo.shape
    # replace overlay pixels with watermark pixel values
    overlay = np.zeros((rows, cols, 4), dtype='uint8')
    for i in range(0, watermark_h):
        for j in range(0, watermark_w):
            if logo[i,j][3] != 0:
                offset = 50
                h_offset = rows - watermark_h - offset
                w_offset = cols - watermark_w - offset
                overlay[h_offset + i, w_offset+ j] = logo[i,j]

    cv2.addWeighted(overlay, 0.25, frame, 1.0, 0, frame)
    cv2.imshow('window-name',frame)
    ##cv2.imwrite("frame%d.jpg" % count, frame)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows