''' GUI for Random Group Creator using QT '''

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from random_gui import Ui_MainWindow

class MyQtApp(QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyQtApp()
    window.show()

    sys.exit(app.exec())
