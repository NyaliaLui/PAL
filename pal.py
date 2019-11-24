# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Nyalia Lui\Documents\GitHub\PAL\QtUI\PAL.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pal import Analyzer
import threading
from queue import Queue

EXQUEUE = Queue()

def valid_sc2name(name):
    invalid_chars = ('-', '&', ' ', '>', '<', '$', '%', '!')
    ret = True

    for ic in invalid_chars:
        ret = (ic not in name and ret)

    return ret and name != ''

class PalThread(QtCore.QThread):

    def set_widget(self, widget):
        self.__widget = widget

    def set_params(self, folder, rate, sc2name):
        self.__folder = folder
        self.__rate = rate
        self.__sc2name = sc2name

    def run(self):
        try:
            #run the ladder analyzer
            analyzer = Analyzer(self.__folder, self.__rate, self.__sc2name)
            analyzer.run()
        except Exception as ex:
            QtWidgets.QMessageBox.critical(self.__widget, 'PAL Error Notification', str(ex), QtWidgets.QMessageBox.Ok)


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
        self.leRate.textChanged.connect(self.update_rate)
        self.__rate = 60
        self.btnRateUp.clicked.connect(self.increase_rate)
        self.btnRateDown.clicked.connect(self.decrease_rate)
        self.btnCollect.clicked.connect(self.start_collection)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCollect.setText(_translate("MainWindow", "Start Collection"))
        self.lblFolder.setText(_translate("MainWindow", "Replay Folder:"))
        self.lblName.setText(_translate("MainWindow", "SC2 Name:"))
        self.lblRate.setText(_translate("MainWindow", "Collect data every X seconds:"))
        self.leName.setToolTip(_translate("MainWindow", "Noticals"))
        self.leRate.setToolTip(_translate("MainWindow", "60"))
        self.leRate.setText(_translate("MainWindow", "60"))
        self.lblHeader.setText(_translate("MainWindow", "SC2 PAL"))
        self.btnFolder.setText(_translate("MainWindow", "Push to select replay folder"))
        self.btnRateUp.setText(_translate("MainWindow", "U"))
        self.btnRateDown.setText(_translate("MainWindow", "D"))

    def set_pal_thread(self, thr):
        self.__pal_thread = thr

    def select_folder(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(parent=self, caption='Select Folder of SC2 Replays')
        self.btnFolder.setText(folder_path)

    def update_rate(self):
        rate = self.leRate.text()

        if rate.isnumeric():
            self.__rate = int(rate)
            self.leRate.setText(rate)

    def increase_rate(self):
        self.__rate += 10
        self.leRate.setText(str(self.__rate))

    def decrease_rate(self):
        self.__rate -= 10
        self.leRate.setText(str(self.__rate))

    def start_collection(self):
        msg = ''
        folder = self.btnFolder.text()
        sc2name = self.leName.text()

        if folder == '' or folder == ' ' or folder == 'Push to select replay folder':
            msg += 'Please input the path to your SC2 Replay folder\n'

        if not valid_sc2name(sc2name):
            msg += 'Please input a valid SC2 player name\n'
        
        if self.__rate < 1:
            msg += 'Collection rate must be 1 or greater\n'

        if msg == '':
            print('Starting PAL with following parameters: ', {'Replay Folder': folder, 'SC2 Name': sc2name, 'Collection Rate': self.__rate})

            try:
                self.__pal_thread.set_params(folder, self.__rate, sc2name)
                self.__pal_thread.start()
            except Exception as ex:
                print('Something went wrong: {0}'.format(str(ex)))
                msg = str(ex)
                QtWidgets.QMessageBox.critical(self, 'PAL Error Notification', msg, QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.critical(self, 'PAL Error Notification', msg, QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys

    #init MainWindow
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    #Create Pal Thread for running the CLI
    pal_thread = PalThread()
    pal_thread.set_widget(MainWindow)
    pal_thread.finished.connect(app.exit)

    #Finish MainWindow Setup
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.set_pal_thread(pal_thread)
    MainWindow.show()
    sys.exit(app.exec_())
