''' Module used to work with .json roster files. '''

import json

def add_roster():
    ''' Enter student names to create a period's roster. '''
    period_name = input('Which period? ')
    roster = []
    print('Type exit to quit.')
    while True:
        name = input('Student? ')
        if name == 'exit':
            break
        roster.append(name)
    
    filename = f'{period_name.title()}.json'
    with open(filename, 'w') as f:
        json.dump(roster,f)
    print(f'Congratulations, you added roster {period_name.title()}.')

def load_roster(period = 'second'):
    ''' Load and return a period's roster. '''
    period_name = period
    filename = f'{period_name.title()}.json'
    with open(filename) as f:
        roster = json.load(f)
    return roster

def edit_roster():
    ''' Edit a pre-existing roster. '''
    period_name = input('Which period? ')
    filename = f'{period_name.title()}.json'
    with open(filename) as f:
        roster = json.load(f)
    print(roster)
    change_from = input('Which name would you like to change? ' )
    change_to = input(f'What would you like to change {change_from} to? ')
    roster[roster.index(change_from)] = change_to
    with open(filename, 'w') as g:
        json.dump(roster,g)
    print(f'Congratulations, you changed {change_from} to {change_to}.')

def update_roster():
    ''' Re-write roster from given list. '''
