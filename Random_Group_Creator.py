''' This will (eventually) be the GUI for the Random Group Creator '''

from roster_ops import add_roster, load_roster
from randomize_groups import rand_roster

print('Hello, this is Random Group Creator!')

choice = input('Do you want to add a roster, load a roster, or shuffle a roster? ')

if choice == 'Add':
    add_roster()
elif choice == 'Load':
    print(load_roster())
elif choice == 'Shuffle':
    roster = load_roster()
    print(roster)
    roster = rand_roster(roster)
    print(roster)
else:
    print('Sorry, that answer didn\'t make sense to me.')