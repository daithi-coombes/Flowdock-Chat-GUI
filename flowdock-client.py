from PyQt4 import QtCore, QtGui
from ui.mainwindow import MainWindow

if __name__ == "__main__":
    import sys,  flowdockClient
    
    flowdockClient.flowdock_py()
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
