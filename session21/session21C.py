"""
    DoctorsApp
"""

# View + Controller

from session21 import Patient
from session21A import Consultation
from session21B import DBHelper
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

            elif choice == 4:           # Fetch All Patients
                sql_query = "select * from patient"
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(row)

            elif choice == 5:          # Fetch patient by phone number
                phone_number = input('Enter patient phone number: ')
                sql_query = "select * from Patient where phone = '{}'".format(phone_number)
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(rows)

                    patient = Patient()
                    patient.patient_id = row[0]
                    patient.name = row[1]
                    patient.phone = row[2]
                    patient.email = row[3]
                    patient.address = row[4]
                    patient.dob = row[5]
                    patient.gender = row[6]
                    patient.created_on = row[7]

                     # print(row)
                    patient.show()

            elif choice == 6:           # Fecth male patient
                 sql_query = "select * from Patient where gender = '{}'".format("Male")
                 rows = self.db_helper.read(sql_query)
                 for row in rows:
                     print(row)
            
            elif choice == 7:           # Fecth female patient
                 sql_query = "select * from Patient where gender = '{}'".format("Female")
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
                patient_id = 0
                answer = input("Do you have patient id (Yes/No):")
                if answer == 'yes':
                    patient_id = int(input('Enter patient id:'))
                else:
                    phone_number = int(input('Enter Patient Phone Number:'))
                    sql_query = "select * from Patient where phone = '{}'".format(phone_number)
                    rows = self.db_helper.read(sql_query)

                    if len(rows) == 1:    # 3 Means ek hi phone number exist krega uniq so row bhi ek hi hogi
                      patient_id = rows[0][0]     # 0 will be row and 0 will be colmn of patient id
                      print('records found',rows[0][1])

                    else:
                        print('Sorry! No such records found')

                if patient_id != 0:       
                    consultation = Consultation()
                    consultation.input_consultation_details()
                    consultation.patient_id = patient_id
                    
                    
                    sql_query = "insert into Consultation values(null,'{}','{}','{}','{}','{}')".format(
                        consultation.patient_id,
                        consultation.remarks,
                        consultation.medicines,
                        consultation.followup,
                        consultation.created_on
                    )
                    self.db_helper.write(sql_query)        # To write consultation
                else:
                    print('Consultation Cannot be Created without Patient ID :')

            elif choice == 2:                 #  Update Existing Consultation
        
                pass
            elif choice == 3:                   # Delete Existing Consultation
                consultation_id = int(input('Enter consultation_id:'))
                sql_query = "delete from Consultation where consultation_id = {}".format(consultation_id)
                self.db_helper.write(sql_query)
                
            elif choice == 4:                   # Fetch All Consultations
                sql_query = "select * from Consultation"
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(row)
                

            elif choice == 5:                    # Fetch consultaion of a patient
                patient_id = int(input('Enter patient id:'))
                sql_query = "select * from Consultation where patient_id = {}".format(patient_id) 
                rows = self.db_helper.read(sql_query)
                for row in rows:
                    print(row)
                
            elif choice == 0:
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                print('Consultation Menu Opened')
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('Enter Suitable Menu Option...')