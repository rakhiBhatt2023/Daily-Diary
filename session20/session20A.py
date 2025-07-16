"""
    DoctorsApp
"""

# View + Controller

from session_20 import Patient
from session20 import DBHelper
import datetime

class DoctorsApp:

    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Welcome to Doctors App')
        print('App Started at: ', datetime.datetime.now())
        print('~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        # doctorsapp has a dbhelper
        self.db_helper = DBHelper()            # object of db helper in session 20 so that connection would be created to database

    def show_main_menu(self):

        while True:

            print('Main Menu: ')
            print('1: Patient')
            print('2: Consulatation')
            print('0: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                self.show_patient_menu()
            elif choice == 2:
                self.show_consultation_menu()
            elif choice == 0:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Thank You for using Doctors App')
                print('App Closed at: ', datetime.datetime.now())
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                self.db_helper.close()                   # so that connection closed when quit the app
                break
            else:
                print('Enter Suitable Menu Option...')


    def show_patient_menu(self):

        print('~~~~~~~~~~~~~~~~~~~~~~')
        print('Patient Menu Opened')
        print('~~~~~~~~~~~~~~~~~~~~~~')

        while True:
            print('Patient Menu: ')
            print('1: Add New Patient')
            print('2: Update Existing Patient')
            print('3: Delete Existing Patient')
            print('4: Fetch All Patients')
            print('5: Fetch Patient by Phone Number')
            print('6: Fetch Male Patients')
            print('7: Fetch Female Patients')
            print('8: Fetch Patients by Created On Date (Sort)')
            print('0: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                patient = Patient()
                patient.input_patient_details()
                sql_query = "insert into Patient values(null,'{}','{}','{}','{}','{}','{}','{}')".format( patient.name, patient.phone, patient.email, patient.address, patient.dob, patient.gender, patient.created_on)
                self.db_helper.write(sql_query)

            elif choice == 2:
                pass

            elif choice == 3:
                patient_id = int(input('Enter patient id:'))
                sql_query = 'Delete from Patient where patient_id = {}'.format(patient_id)
                self.db_helper.write(sql_query)                

            elif choice == 4:
                sql_query = "select * from patient"
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(row)

            elif choice == 0:
                print('~~~~~~~~~~~~~~~~~~~~~~')
                print('Patient Menu Closed')
                print('~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('Enter Suitable Menu Option...')

    def show_consultation_menu(self):

        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Consultation Menu Opened')
        print('~~~~~~~~~~~~~~~~~~~~~~~~')

        while True:
            print('Consultation Menu: ')
            print('1: Add New Consultation')
            print('2: Update Existing Consultation')
            print('3: Delete Existing Consultation')
            print('4: Fetch All Consultation')
            print('5: Fetch Consultation of a Patient')
            print('0: Quit')
            choice = int(input('Enter Your Choice: '))
            
            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 0:
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Consultation Menu Opened')
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('Enter Suitable Menu Option...')