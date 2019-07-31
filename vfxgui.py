from PySide2 import QtWidgets
from roster_ops import load_roster
from populate_list import populate_list1, populate_list2, populate_list3, populate_list4, populate_list5, populate_list6

import random_gui

class MyQtApp(random_gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        self.current_period = 'Second'
        self.populate_lists(self.current_period)
        self.select_period_CB.activated.connect(self.update_period)
        self.select_period_CB.activated.connect(self.update_lists)
        self.update_period()
        self.update_lists()
        self.randomize_PB.clicked.connect(self.rand_groups_now)
        self.rand_groups_now()

    def populate_lists(self,current_period):
        populate_list1(self,current_period)
        populate_list2(self,current_period)
        populate_list3(self,current_period)
        populate_list4(self,current_period)
        populate_list5(self,current_period)
        populate_list6(self,current_period)

    def update_period(self):
        if self.select_period_CB.activated:
            self.current_period = self.select_period_CB.currentText()
            print(self.current_period)

    def update_lists(self):
        if self.current_period == '2nd':
            self.populate_lists('Second')
        if self.current_period == '3rd':
            self.populate_lists('Third')
        if self.current_period == '4th':
            self.populate_lists('Fourth')
        if self.current_period == '5th':
            self.populate_lists('Fifth')

    def rand_groups_now(self):
        if self.randomize_PB.clicked:
            print('Hello')

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
