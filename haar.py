#import numpy as np
import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import QWidget, QFileDialog

class Haar(QWidget):
        def init(self):
                super().__init__()
                self.setWindowTitle("PyQt5 Media Player")
                self.setGeometry(350, 100, 700, 500)
                self.setWindowIcon(QIcon('player.png'))

                p = self.palette()
                p.setColor(QPalette.Window, Qt.white)
                self.setPalette(p)

        def haar(self):
                filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
                cap= cv2.VideoCapture('C:/Users/aniru/Desktop/vtest.avi')
                #fourcc=cv2.VideoWriter_fourcc(*'XVID')
                #out=cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640,480))
                #hog = cv2.HOGDescriptor()
                #hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
                body_cascade=cv2.CascadeClassifier('E:/Program Files/Python38/Lib/site-packages/cv2/data/haarcascade_fullbody.xml')

                while((cap.isOpened)):
                        ret,frame=cap.read()
                       # frame = imutils.resize(frame, width=100)
                        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

                        bodies = body_cascade.detectMultiScale(gray,1.1,3)
                        #body_cascade.detectMultiScale()
                        for (x,y,w,h) in bodies:
                                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

                         #out.write(frame)
                     #cv2.imshow('frame', frame)
                                cv2.imshow('gray', frame)
                        if cv2.waitKey(12) & 0xFF== ord('q'):
                                break
                cap.release()
                #out.release()
                cv2.destroyAllWindows()