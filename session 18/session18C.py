"""
    Application

"""
# Model
from session18A import Visitor

# Controller
from session18B import FileHelper


# View + controller
class VisitorApp:


    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Welcome to Visitor Log book App')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        # create a file helper object, which is an attribute of visitorapp
        # Has-A Relationship

        self.file_helper = FileHelper()
        #print('File Size:', self.file_helper.file_size(), 'bytes')

    def show_menu(self):
         

         while True:
            print('~~~~~~~~~~~Select Option~~~~~~~~~')
            print('1. Log a visit')
            print('2. view visit log book')
            print('3. Quit')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            choice = int(input('Enter your choice:'))


            if choice ==1:
                print('Add a new Visitor log:')
                self.add_visitor()
            elif choice ==2 :
                print('View visit logbook')
                self.view_all_visitors()
            elif choice == 3:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('thank you for using visitor App')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                 print("Invalid Menu Option")

    def add_visitor(self):
            # 1. create an empty visitor
            visitor = Visitor()
            # 2. Take inputs
            visitor.visitor_details()
            # 3. Save visitor in file
            visitor.serial_no = self.file_helper.lines_in_file()
            self.file_helper.write_in_file(content = str(visitor))

    def view_all_visitors(self):
            self.file_helper.read_file()





   