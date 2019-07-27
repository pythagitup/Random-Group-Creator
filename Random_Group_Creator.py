''' This will (eventually) be the GUI for the Random Group Creator '''

from roster_ops import add_roster, load_roster, edit_roster
from randomize_groups import rand_roster, six_groups

print('Hello, this is Random Group Creator!\nType "exit" at any time to quit.')

while True:
    choice = input('Do you want to add a roster, load a roster, edit a roster, shuffle a roster, or create groups? ')
    choice = choice.lower()
    if choice == 'exit':
        break
    elif choice == 'add':
        add_roster()
    elif choice == 'load':
        print(load_roster())
    elif choice == 'edit':
        edit_roster()
    elif choice == 'shuffle':
        roster = load_roster()
        print(roster)
        roster = rand_roster(roster)
        print(roster)
    elif choice == 'groups':
        roster = load_roster()
        print(roster)
        roster = rand_roster(roster)
        six_groups(roster)
    else:
        print('Sorry, that answer didn\'t make sense to me.')