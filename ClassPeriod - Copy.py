from random import shuffle
from roster_ops import load_roster

class ClassPeriod:
    ''' Class to hold roster, randomize it, and make groups. '''

    def __init__(self):
        self.roster = []
        self.period = ''

    def set_period(self,period):
        ''' Set the period. '''
        self.period = period

    def set_roster(self):
        ''' Load roster for this period. '''
        self.roster = load_roster(self.period)

    def show_roster(self):
        ''' Print the roster. '''
        print(self.roster)

    def randomize(self):
        ''' Randomize the roster. '''
        shuffle(self.roster)

    def groups(self,number_groups):
        ''' Split class into given number of groups. '''
        x = number_groups
        y = []
        for i in range(x):
            y.append([])
        for j in range(len(self.roster)):
            m = j % x
            y[m].append(self.roster[j])
        return y
        
    def display_groups(self,number_groups):
        x = number_groups
        y = self.groups(number_groups)
        for k in range(x):
            print(f'Group {k+1}: ')
            for name in y[k]:
                print(name)