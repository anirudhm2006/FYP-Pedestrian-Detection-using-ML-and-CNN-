# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from TestVideoOpen import Window
from HOG import Hog
from haar import Haar
from cnn_rough import cnn

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuML = QtWidgets.QMenu(self.menubar)
        self.menuML.setObjectName("menuML")
        self.menuSVM = QtWidgets.QMenu(self.menuML)
        self.menuSVM.setObjectName("menuSVM")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionK_NN = QtWidgets.QAction(MainWindow)
        self.actionK_NN.setObjectName("actionK_NN")
        self.actionCNN = QtWidgets.QAction(MainWindow)
        self.actionCNN.setObjectName("actionCNN")
        self.actionHOG = QtWidgets.QAction(MainWindow)
        self.actionHOG.setObjectName("actionHOG")
        self.actionHAAR = QtWidgets.QAction(MainWindow)
        self.actionHAAR.setObjectName("actionHAAR")
        self.menuFile.addAction(self.actionOpen)
        self.menuSVM.addAction(self.actionHOG)
        self.menuSVM.addAction(self.actionHAAR)
        self.menuML.addAction(self.menuSVM.menuAction())
        self.menuML.addAction(self.actionK_NN)
        self.menuML.addAction(self.actionCNN)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuML.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionOpen.triggered.connect(self.show_popup)
        self.actionHOG.triggered.connect(self.show)
        self.actionHAAR.triggered.connect(self.show_haar)
        self.actionCNN.triggered.connect(self.show_cnn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuML.setTitle(_translate("MainWindow", "ML"))
        self.menuSVM.setTitle(_translate("MainWindow", "SVM"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionK_NN.setText(_translate("MainWindow", "K-NN"))
        self.actionCNN.setText(_translate("MainWindow", "CNN"))
        self.actionHOG.setText(_translate("MainWindow", "HOG"))
        self.actionHAAR.setText(_translate("MainWindow", "HAAR"))

    def show_popup(self):
        self.ChildWin = Window()
        self.ChildWin.init()

    def show(self):
        self.ChildHog = Hog()
        self.ChildHog.init()
        self.ChildHog.svm_hog()

    def show_haar(self):
        self.ChildHaar = Haar()
        self.ChildHaar.init()
        self.ChildHaar.haar()

    def show_cnn(self):
        self.Childcnn= cnn()
        self.Childcnn.init()
        self.Childcnn.Cnn()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
