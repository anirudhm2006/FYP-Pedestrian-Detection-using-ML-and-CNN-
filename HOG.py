#import numpy as np
import sys
import cv2
#from TestVideoOpen import Window
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from TestVideoOpen import Window

class Hog(QWidget):
    def init(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('player.png'))

        p = self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)

       # self.init_ui()

        #self.show()

    def svm_hog(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        cap = cv2.VideoCapture(filename)
       # cap= cv2.VideoCapture('C:/Users/aniru/Desktop/vtest.avi')
        #fourcc=cv2.VideoWriter_fourcc(*'XVID')
        #out=cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640,480))
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        while((cap.isOpened)):
                ret,frame=cap.read()
                gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

                (rects,weights) = hog.detectMultiScale(gray,winStride=(4,4),padding=(8,8),scale=1.05)
                for (x,y,w,h) in rects:
                        cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)

                 #out.write(frame)
             #cv2.imshow('frame', frame)
                        cv2.imshow('gray', gray)
                if cv2.waitKey(25) & 0xFF== ord('q'):
                    break

        cap.release()
        #out.release()
        cv2.destroyAllWindows()

#app = QApplication(sys.argv)
#hog = Hog()
#hog.init()
#hog.svm_hog()
#sys.exit(app.exec_())