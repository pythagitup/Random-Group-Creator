from random import shuffle

class ClassPeriod:
    ''' Class to hold roster, randomize it, and make groups. '''

    def __init__(self,roster):
        self.roster = roster

    def show_roster(self):
        ''' Print the roster. '''
        print(self.roster)

    def randomize(self):
        ''' Randomize the roster. '''
        shuffle(self.roster)
        print(self.roster)

    def groups(self,number_groups):
        ''' Split class into given number of groups. '''
        x = number_groups
        y = []
        for i in range(x):
            y.append([])
        for j in range(len(self.roster)):
            m = j % x
            y[m].append(self.roster[j])
        for k in range(x):
            print(f'Group {k+1}: ')
            for name in y[k]:
                print(name)