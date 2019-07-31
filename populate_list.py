from ClassPeriod import ClassPeriod
from roster_ops import load_roster

def populate_list1(self,period):
    self.group1_L.clear()
    roster = load_roster(period)
    x = ClassPeriod(roster)
    y = x.groups(6)
    for i in range(len(y[0])):
        self.group1_L.insertItem(i,y[0][i])

def populate_list2(self,period):
    self.group2_L.clear()
    roster = load_roster(period)
    x = ClassPeriod(roster)
    y = x.groups(6)
    for i in range(len(y[1])):
        self.group2_L.insertItem(i,y[1][i])

def populate_list3(self,period):
    self.group3_L.clear()
    roster = load_roster(period)
    x = ClassPeriod(roster)
    y = x.groups(6)
    for i in range(len(y[2])):
        self.group3_L.insertItem(i,y[2][i])

def populate_list4(self,period):
    self.group4_L.clear()
    roster = load_roster(period)
    x = ClassPeriod(roster)
    y = x.groups(6)
    for i in range(len(y[3])):
        self.group4_L.insertItem(i,y[3][i])

def populate_list5(self,period):
    self.group5_L.clear()
    roster = load_roster(period)
    x = ClassPeriod(roster)
    y = x.groups(6)
    for i in range(len(y[4])):
        self.group5_L.insertItem(i,y[4][i])

def populate_list6(self,period):
    self.group6_L.clear()
    roster = load_roster(period)
    x = ClassPeriod(roster)
    y = x.groups(6)
    for i in range(len(y[5])):
        self.group6_L.insertItem(i,y[5][i])