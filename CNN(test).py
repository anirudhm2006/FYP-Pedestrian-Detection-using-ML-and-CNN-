import numpy as np
import cv2
# import pickle
import os
import h5py
from keras.models import load_model
from keras.models import load_model
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QPalette
from PyQt5.QtWidgets import QWidget,QFileDialog
from TestVideoOpen import Window
import sys
# import numpy as np

class cnn(QWidget):

    def init(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('player.png'))
        p = self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)

    def Cnn(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        cap = cv2.VideoCapture(filename)
        ########### PARAMETERS ##############
        width = 640
        height = 480
        threshold = 0.65  # MINIMUM PROBABILITY TO CLASSIFY
        # cameraNo = 1
        count = 0
        #####################################

        #### CREATE CAMERA OBJECT

        path = "E:/backupimage folder"

        # path = "E:/Final ML project/Dogs_Cats_2000pics_train/0"

        #### LOAD THE TRAINNED MODEL

        # fname = "E:/Final ML project/test2_89percent.h5"

        # fname = "E:/Final ML project/test2_10epoch50batchsize_50steps_weights.h5"

        # fname = "E:/Final ML project/DogsCats_10epoch100batchsize_100steps_weights.h5"

        fname = "E:/Final ML Project/humans_train_weights.h5"  # ani
        # fname = "E:/Final ML Project/humans_train_weights_50batch_50steps.h5"#ani
        # fname = "E:/Final ML Project/humans_train_weights_100batch_30steps.h5"#ani

        # fname = "E:/Final ML project/test2_10epoch100batchsize_100steps_weights_89percent.h5"

        # fname = "E:/Final ML project/test2_50epoch_weights.h5"

        # fname = "E:/Final ML project/test2_100epoch_weights.h5"

        model = load_model(fname)


        #### PREPORCESSING FUNCTION

        def preProcessing(img):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.equalizeHist(img)
            img = img / 255
            return img


        myPicList = os.listdir(path)
        classindex = []
        probval = []
        # listp=[]
        # listq=[]

        for y in myPicList:
            curImg = cv2.imread(path + "/" + y)

            image = curImg

            img = np.asarray(curImg)
            curImg = cv2.resize(curImg, (64, 64))
            img = preProcessing(curImg)
            img = img.reshape(1, 64, 64, 1)

            classIndex = int(model.predict_classes(img))
            # print(predictions)
            predictions = model.predict(img)

            probVal = np.amax(predictions)
            print(classIndex, probVal)

            if probVal > threshold:
                cv2.putText(image, str(classIndex) + " " + str(probVal),
                            (0, 30), cv2.FONT_HERSHEY_COMPLEX,
                            1, (0, 0, 255), 1)
            # print("ProbVal > Threshold")

            classindex.append(classIndex)
            probval.append(probVal)
            p = classindex.count(3)
            # q=classindex.count(1)
            cv2.imshow("Original Image", image)

            if cv2.waitKey(0) & 0xFF == ord('q'):
                print("the count of class 3 is:", p)
                # print("the count of class 1 is:", q)
                # print(probval)
                # print(len(probval))
                # print(len(classindex))
                # print(len(probval))
                mean = sum(probval) / len(probval)
                print(mean)
                break
        mean = sum(probval) / len(probval)
        print("mean=", mean)
        p = classindex.count(0)
        q = classindex.count(1)
        r = classindex.count(2)
        s = classindex.count(3)
        print("the count of class 0 is:", p)
        print("the count of class 1 is:", q)
        print("the count of class 2 is:", r)
        print("the count of class 3 is:", s)
        # print(probval)
