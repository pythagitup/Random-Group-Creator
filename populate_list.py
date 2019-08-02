from ClassPeriod import ClassPeriod

def populate_lists(self,period,rand=False):
    self.group1_L.clear()
    self.group2_L.clear()
    self.group3_L.clear()
    self.group4_L.clear()
    self.group5_L.clear()
    self.group6_L.clear()
    x = ClassPeriod()
    x.set_period(period)
    x.set_roster()
    if rand:
        x.randomize()
    y = x.groups(6)
    for i in range(len(y[0])):
        self.group1_L.insertItem(i,y[0][i])
    for i in range(len(y[1])):
        self.group2_L.insertItem(i,y[1][i])
    for i in range(len(y[2])):
        self.group3_L.insertItem(i,y[2][i])
    for i in range(len(y[3])):
        self.group4_L.insertItem(i,y[3][i])
    for i in range(len(y[4])):
        self.group5_L.insertItem(i,y[4][i])
    for i in range(len(y[5])):
        self.group6_L.insertItem(i,y[5][i])