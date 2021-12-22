# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtCore import QTimer
import time,datetime
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def __init__(self):
        self.image_counter = 0
        self.frame_count = 1
        self.Paused = True
        self.x = ''

    def setupUi(self, MainWindow):

        self.__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(20, 540, 75, 23))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start_webcam)

        self.PauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.PauseButton.setGeometry(QtCore.QRect(100, 540, 75, 23))
        self.PauseButton.setObjectName("PauseButton")
        self.PauseButton.clicked.connect(self.Pause)

        self.capture = QtWidgets.QPushButton(self.centralwidget)
        self.capture.setGeometry(QtCore.QRect(200, 540, 75, 23))
        self.capture.setObjectName("capture")
        self.capture.clicked.connect(self.capture_image)

        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(1, 1, 640, 480))
        self.imgLabel.setObjectName("imgLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.imgLabel.mousePressEvent = self.ImgMouseClick
        self.imgLabel.mouseMoveEvent = self.ImgMouseMoveEvent
        self.imgLabel.mouseReleaseEvent = self.ImgMouseButtonUp

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update_frame)
        # self.timer.start(100)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.start_webcam()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "startButton"))
        self.capture.setText(_translate("MainWindow", "capture"))
        self.imgLabel.setText(_translate("MainWindow", "imgLabel"))
        self.PauseButton.setText(_translate("MainWindow", "Play"))

    def ImgMouseMoveEvent(self, evt):
       # print("Mouse Moved to ", evt.x(), evt.y())

        image2 = self.Imgframe.copy()
        cv2.rectangle(image2, (self.startX, self.startY), (evt.x(), evt.y()), (0, 0, 255), 2)
        #cv2.imshow("test", image2)
        self.displayImage(image2, True)
        self.EndX = evt.x()
        self.EndY = evt.y()

    def ImgMouseClick(self, evt):
        #self.Pause()
        #print("LeftMouseButtonClicked")
      #  print("Mouse Clicked at: ",evt.x(), evt.y())
        self.startX = evt.x()
        self.startY = evt.y()

    def ImgMouseButtonUp(self, evt):

        #print ("Mouse Button Released at: ", evt.x(), evt.y())
        cv2.rectangle(self.Imgframe, (self.startX, self.startY), (self.EndX, self.EndY), (0, 255, 255), 3)
        self.displayImage(self.Imgframe, True)
        self.croppedImage = self.Imgframe[ self.startY:self.EndY, self.startX:self.EndX]

        print("Cropped Image Shape: ", self.croppedImage.shape)
        # d = datetime.datetime.now()
        # s = getattr(d,'year'), getattr(d,'month')
        # st = str(s[0]) + str(s[1])
        # print(st)
        #
        # for attr in ['year', 'month', 'day', 'hour', 'minute']:
        #     print (attr, ':', getattr(d, attr))

        self.croppedImage = cv2.resize(self.croppedImage, (100,300), interpolation=cv2.INTER_AREA )
        cv2.imshow("croppedImage", self.croppedImage)
        self.image_counter += 1
        self.x = time.strftime('%d-%m-%Y_%H-%M')
        filename = "E:/test_{}_{}.png".format(self.image_counter,self.x)
        cv2.imwrite(filename,self.croppedImage)

       # flag,croppedImage = self.capture.read()
       # path = 'E:/training_data'
        #if flag:
         #   name = "trainpictures_{}.png".format(self.image_counter)
          #  cv2.imwrite(os.path.join(path, name), self.croppedImage)

    def Pause(self):
        if self.Paused:
            self.timer.start(40)
            self.Paused = False
            self.PauseButton.setText("Pause")
        else:
            self.timer.stop()
            self.Paused = True
            self.PauseButton.setText("Play")
            #_, self.Imgframe = self.capture.read()
            self.Imgframe = self.glImage

            width = int(480 * self.Imgframe.shape[1]/self.Imgframe.shape[0])
            height = 480
            self.Imgframe = cv2.resize(self.Imgframe, (width,height), interpolation= cv2.INTER_AREA)

       # cv2.rectangle(self.Imgframe, (0,0), (200,200), (0,0,255), 1)
      #  cv2.imshow("test", frame)
      #  self.displayImage(self.Imgframe,True)

    def start_webcam(self):
        print("webcam started")
        filename, _ = QFileDialog.getOpenFileName(MainWindow, "Open")
        self.capture = cv2.VideoCapture(filename)
        ret, frm = self.capture.read()
        print("Originial Image: ",frm.shape)

        #cv2.imshow('title', frm)

        width = int (480 * frm.shape[1]/frm.shape[0])
        height = 480

        frm = cv2.resize(frm, (width, height), interpolation= cv2.INTER_AREA)

        # print(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        # self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        # self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

        self.displayImage(frm, True)
       # self.imgLabel.setGeometry(QtCore.QRect(1, 1, frm.shape[1], frm.shape[0]))

        #self.timer.start(100)
        print("Reduced Frame: ",frm.shape)
        self.StartMyTimer()

    def displayImage(self, img, window=True):
        qformat = QtGui.QImage.Format_Indexed8
        if len(img.shape)==3 :
            if img.shape[2]==4:
                qformat = QtGui.QImage.Format_RGBA8888
            else:
                qformat = QtGui.QImage.Format_RGB888
        outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        if window:
            self.imgLabel.setPixmap(QtGui.QPixmap.fromImage(outImage))

    def capture_image(self):
        self.timer.stop()
        print("Capturing...")
        # set position to the last frame
        self.capture.set(1, self.capture.get(cv2.CAP_PROP_FRAME_COUNT) -1)
        ok, frame = self.capture.read()

        # Other image processing and feature extraction
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # edged = cv2.Canny(gray, 100, 300)

        # Draw rectangle on the image
        # cv2.rectangle(frame,(0,0), (200,200),(0,0,255),2)
        #
        # Find contours in the image
        # contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # # Draw contours
        # cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
        # # Show the image
        # cv2.imshow('Contours', frame)

      #  cv2.imshow("frame", edged)

        path = 'F:/'
        if ok:
            # cv2.imshow("frame", frame)
            # Show the image frame in the Parent Window
            self.displayImage(frame,True)
            # QtWidgets.QApplication.beep()
            # name = "test_{}.png".format(self._image_counter)
            # print (name)
            # cv2.imwrite(cv2.os.path.join(path, name), frame)
            # cv2.imwrite('F:/test.png', frame)
            # self._image_counter += 1
            self.timer.start()
        else:
            print("End of File")

    def update_frame(self):
        #print("sfkdd")
        if self.capture.isOpened():
            ret, image = self.capture.read()
            if ret:
                width = int(480 * image.shape[1]/image.shape[0])
                height = 480
                image = cv2.resize(image, (width, height), interpolation= cv2.INTER_AREA)
                self.glImage = image
                #print (image.shape[0], ',' , image.shape[1])
                #simage = cv2.flip(image, 1)
                self.displayImage(image, True)
            else:
                self.capture.release()
                self.timer.stop()
                print("Timer stopped")

    def StartMyTimer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        #self.timer.setInterval(10)
        #self.timer.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())