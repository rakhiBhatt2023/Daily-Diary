"""
    Doctor's App
    ------------
    
    # 1. Think of an Object
    Patient: patient_id, name, phone, email, address, dob, gender, created_on

    ORM Fundamental

    create table Patient(
        patient_id int primary key auto_increment,
        name varchar(256),
        phone varchar(20),
        email varchar(256),
        address text,
        dob date,
        gender varchar(20),
        created_on datetime
    );

"""
import datetime
class Patient:
    def __init__(self, name=None, phone=None, email=None, address = None, dob = None, gender = None):
        self.patient_id = 0
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.dob = dob
        self.gender = gender
        self.created_on = datetime.datetime.now()

    def input_patient_details(self):
        self.name = input('Enter patient name:')
        self.phone = input('Enter phone no:')
        self.email = input('Enter your email:')
        self.address = input('Enter patient address:')
        self.dob = input('Enter patient DOB(yyyy-mm-dd):')
        self.gender = input('Enter patient gender:')

    def show(self):
        print("~~~~~~~~~~Patient~~~~~~~~~~~")
        print('Patient ID:', self.patient_id)
        print('Name:', self.name)
        print('Phone:', self.phone)
        print('Email:', self.email)
        print('Address:', self.address)
        print('DOB:', self.dob)
        print('Gender:', self.gender)
        print('Craeted On:', self.created_on)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    

          
