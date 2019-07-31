from PySide2 import QtWidgets
from roster_ops import load_roster
from populate_list import populate_lists

import random_gui

class MyQtApp(random_gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        self.current_period = '2nd'
        self.select_period_CB.activated.connect(self.update_period)
        self.populate_the_lists(self.current_period)
        self.select_period_CB.activated.connect(self.update_lists)
        self.update_period()
        self.update_lists()
        self.randomize_PB.clicked.connect(self.rand_groups_now)
        self.rand_groups_now()

    def populate_the_lists(self,current_period,rand=False):
        populate_lists(self,current_period,rand)

    def update_period(self):
        if self.select_period_CB.activated:
            self.current_period = self.select_period_CB.currentText()

    def update_lists(self):
        self.populate_the_lists(self.current_period)

    def rand_groups_now(self):
        if self.randomize_PB.clicked:
            self.populate_the_lists(self.current_period,rand=True)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
