''' Module for taking a roster, shuffling students, and creating groups. '''

from random import shuffle

def rand_roster(roster):
    ''' Takes a roster list and shuffles the students. '''
    shuffle(roster)
    return roster

def six_groups(roster):
    ''' Takes a roster list and splits into 6 groups. '''
    group0 = []
    group1 = []
    group2 = []
    group3 = []
    group4 = []
    group5 = []
    groups = [group0, group1, group2, group3, group4, group5]
    for i in range(len(roster)):
        if i % 6 == 0:
            group0.append(roster[i])
        if i % 6 == 1:
            group1.append(roster[i])
        if i % 6 == 2:
            group2.append(roster[i])
        if i % 6 == 3:
            group3.append(roster[i])
        if i % 6 == 4:
            group4.append(roster[i])
        if i % 6 == 5:
            group5.append(roster[i])
    for i in range(len(groups)):
        print(f'Group {i+1}: {groups[i]}\n')