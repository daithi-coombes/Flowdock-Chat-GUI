from PyQt4 import QtCore, QtGui
from ui.mainwindow import MainWindow
import thread
import flowdockClient
import settings

def stream_stdout( stream):
    """
    Acts as callback for messages from stream.
    Routes messages from pycurl stream to the UI
    """
    ui.update_textBrowser( stream )
    

if __name__ == "__main__":
    import sys
    
    #start window
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    
    #start stream as new thread
    flow = flowdockClient.flowdock_py()
    flow.DEBUG = 1
    flow.API_TOKEN = settings.API_TOKEN
    flow.USER = settings.USER    #this is the user email address (user for logging in)
    flow.USER_NAME = settings.USER_NAME     #the display name for the user
    flow.PASS = settings.PASS
    th = thread.start_new_thread(flow.stream, (stream_stdout, ))
    ui.load_flow(flow)
    flow.get_users()

    #show window
    ui.show()
    sys.exit(app.exec_())
