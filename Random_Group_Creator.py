''' Random Group Creator application '''

from roster_ops import add_roster, load_roster, edit_roster
from ClassPeriod import ClassPeriod

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
        x = ClassPeriod(roster)
        x.show_roster()
        x.randomize()
    elif choice == 'groups':
        roster = load_roster('second')
        x = ClassPeriod(roster)
        n = input('How many groups? ')
        x.display_groups(int(n))

    else:
        print('Sorry, that answer didn\'t make sense to me.')