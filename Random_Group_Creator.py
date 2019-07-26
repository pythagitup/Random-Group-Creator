''' This will (eventually) be the GUI for the Random Group Creator '''

from RosterModule import add_roster, load_roster

print('Hello, this is Random Group Creator!')

choice = input('Do you want to add a roster or load a roster? ')

if choice == 'Add':
    add_roster()
elif choice == 'Load':
    print(load_roster())
else:
    print('Sorry, that answer didn\'t make sense to me.')