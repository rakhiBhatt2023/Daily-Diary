"""
    Applicatio

"""

class VisitorApp:
    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Welcome to Visitor Log book App')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


    def show_menu(self):
         
         while True:
            print('~~~~~~~~~~~~~~~Select Option~~~~~~~~~~~~~~~')
            print('1. Log a visit')
            print('2. view visit log book')
            print('3. Quit')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            choice = int(input('Enter your chice:'))

            if choice ==1:
                print('Add a new Visitor log:')
            elif choice ==2 :
                print('View visit logbook')
            elif choice == 3:
                break
            else:
                 print("Invalid Menu Option")





   