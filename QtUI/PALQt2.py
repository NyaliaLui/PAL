# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nyalia Lui\Documents\GitHub\PAL\QtUI\PAL.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(559, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCollect = QtWidgets.QPushButton(self.centralwidget)
        self.btnCollect.setGeometry(QtCore.QRect(20, 410, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnCollect.setFont(font)
        self.btnCollect.setObjectName("btnCollect")
        self.lblFolder = QtWidgets.QLabel(self.centralwidget)
        self.lblFolder.setGeometry(QtCore.QRect(30, 110, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblFolder.setFont(font)
        self.lblFolder.setObjectName("lblFolder")
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(30, 220, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblName.setFont(font)
        self.lblName.setObjectName("lblName")
        self.lblRate = QtWidgets.QLabel(self.centralwidget)
        self.lblRate.setGeometry(QtCore.QRect(30, 330, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblRate.setFont(font)
        self.lblRate.setObjectName("lblRate")
        self.leName = QtWidgets.QLineEdit(self.centralwidget)
        self.leName.setGeometry(QtCore.QRect(200, 220, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leName.setFont(font)
        self.leName.setAutoFillBackground(False)
        self.leName.setObjectName("leName")
        self.leRate = QtWidgets.QLineEdit(self.centralwidget)
        self.leRate.setGeometry(QtCore.QRect(380, 330, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leRate.setFont(font)
        self.leRate.setObjectName("leRate")
        self.lblHeader = QtWidgets.QLabel(self.centralwidget)
        self.lblHeader.setGeometry(QtCore.QRect(30, 20, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lblHeader.setFont(font)
        self.lblHeader.setFrameShape(QtWidgets.QFrame.Box)
        self.lblHeader.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lblHeader.setLineWidth(1)
        self.lblHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeader.setObjectName("lblHeader")
        self.btnFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnFolder.setGeometry(QtCore.QRect(200, 110, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnFolder.setFont(font)
        self.btnFolder.setObjectName("btnFolder")
        self.btnRateUp = QtWidgets.QPushButton(self.centralwidget)
        self.btnRateUp.setGeometry(QtCore.QRect(510, 330, 21, 21))
        self.btnRateUp.setObjectName("btnRateUp")
        self.btnRateDown = QtWidgets.QPushButton(self.centralwidget)
        self.btnRateDown.setGeometry(QtCore.QRect(510, 350, 21, 21))
        self.btnRateDown.setObjectName("btnRateDown")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnFolder.clicked.connect(self.select_folder)
        self.__rate = 60
        self.btnRateUp.clicked.connect(self.increase_rate)
        self.btnRateDown.clicked.connect(self.decrease_rate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCollect.setText(_translate("MainWindow", "Start Collection"))
        self.lblFolder.setText(_translate("MainWindow", "Replay Folder:"))
        self.lblName.setText(_translate("MainWindow", "SC2 Name:"))
        self.lblRate.setText(_translate("MainWindow", "Collect data every X seconds:"))
        self.leName.setToolTip(_translate("MainWindow", "Noticals"))
        self.leRate.setToolTip(_translate("MainWindow", "60"))
        self.leRate.setText(_translate("MainWindow", "60s"))
        self.lblHeader.setText(_translate("MainWindow", "SC2 PAL"))
        self.btnFolder.setText(_translate("MainWindow", "Push to select replay folder"))
        self.btnRateUp.setText(_translate("MainWindow", "U"))
        self.btnRateDown.setText(_translate("MainWindow", "D"))

    def select_folder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(parent=self, caption='Select Folder of SC2 Replays')
        self.btnFolder.setText(folder_path)

    def increase_rate(self):
        self.__rate += 10
        rate = str(self.__rate) + 's'
        print(rate)
        self.leRate.setText(rate)

    def decrease_rate(self):
        self.__rate -= 10
        rate = str(self.__rate) + 's'
        print(rate)
        self.leRate.setText(rate)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
