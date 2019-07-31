from PySide2 import QtWidgets
from roster_ops import load_roster
from ClassPeriod import ClassPeriod
from populate_list import populate_list1, populate_list2, populate_list3, populate_list4, populate_list5, populate_list6

import random_gui

class MyQtApp(random_gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp,self).__init__()
        self.setupUi(self)
        self.current_period = 'Second'
        self.populate_lists(self.current_period)

    def populate_lists(self,current_period):
        populate_list1(self,current_period)
        populate_list2(self,current_period)
        populate_list3(self,current_period)
        populate_list4(self,current_period)
        populate_list5(self,current_period)
        populate_list6(self,current_period)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
