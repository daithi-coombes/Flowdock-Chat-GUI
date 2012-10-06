# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_mainwindow import Ui_MainWindow
import thread,  flowdockClient,  json

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
    def load_flow(self,  flow):
        self.flow = flow
    
    def update_textBrowser(self,  data):
        """
        Updates the receive text box
        """
        self.textRecv.append(data)
    
    @pyqtSignature("")
    def on_btnSend_released(self):
        """
        Takes text from send text box and posts it to flowdock_py::stream_requests
        QTextedit documentation: http://qt-project.org/doc/qt-4.8/QTextEdit.html
        """
        data = self.textSend.toPlainText()
        self.flow.stream_requests( data )
        self.textSend.clear()
        pass
