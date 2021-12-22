import cv2
import numpy as np
from PyQt5.QtWidgets import QFileDialog, QWidget
import sys

cap = cv2.VideoCapture("C:/Users/aniru/Desktop/vtest.avi")
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))
ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
  #  _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)
    imgThresh = cv2.adaptiveThreshold(blur,  # input image
                                  255,  # make pixels that pass the threshold full white
                                  cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  # use gaussian rather than mean, seems to give better results
                                  cv2.THRESH_BINARY_INV,  # invert so foreground will be white, background will be black
                                  11,  # size of a pixel neighborhood used to calculate threshold value
                                  2)  # constant subtracted from the mean or weighted mean



# dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(imgThresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 1000:
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 3)
            cv2.drawContours(frame1, contours, 0, (0, 255, 0), 2)

    image = cv2.resize(frame1, (1280,720))
    out.write(image)
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()
