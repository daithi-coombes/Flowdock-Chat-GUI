# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/var/www/flowdock/python/flowdock-client/ui/mainwindow.ui'
#
# Created: Thu Oct  4 02:03:57 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(365, 464)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.btnSend = QtGui.QPushButton(self.centralWidget)
        self.btnSend.setGeometry(QtCore.QRect(80, 420, 98, 27))
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.textRecv = QtGui.QTextEdit(self.centralWidget)
        self.textRecv.setGeometry(QtCore.QRect(10, 11, 256, 311))
        self.textRecv.setObjectName(_fromUtf8("textRecv"))
        self.textSend = QtGui.QTextEdit(self.centralWidget)
        self.textSend.setGeometry(QtCore.QRect(10, 340, 256, 61))
        self.textSend.setObjectName(_fromUtf8("textSend"))
        self.toolBtn = QtGui.QPushButton(self.centralWidget)
        self.toolBtn.setGeometry(QtCore.QRect(280, 60, 61, 27))
        self.toolBtn.setObjectName(_fromUtf8("toolBtn"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSend.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBtn.setText(QtGui.QApplication.translate("MainWindow", "Tool btn", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

