import json

def add_roster():
    period_name = input('Which period? ')
    roster = []
    print('Type exit to quit.')
    while True:
        name = input('Student? ')
        if name == 'exit':
            break
        roster.append(name)
    
    filename = f'{period_name}.json'
    with open(filename, 'w') as f:
        json.dump(roster,f)
    print(f'Congratulations, you added roster {period_name}.')

def load_roster():
    period_name = input('Which period? ')
    filename = f'{period_name}.json'
    with open(filename) as f:
        roster = json.load(f)
    return roster