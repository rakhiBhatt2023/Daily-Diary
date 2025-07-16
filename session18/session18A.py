"""
     Think of an object
     Visitor  : serial_no, date_time_stamp, name, phone, address, whome_to_meet purpose 
     Customer : name, phone, address, points
     Patient  : name, phone, email, address, weight,height, bp_high, bp_low, sugar
      
"""

# MODEL using OOPS
import datetime

class Visitor:
    def __init__(self,serial_no = None, name=None, phone=None, address=None, whome_to_meet=None, purpose=None ):
        self.serial_no = serial_no
        self.name  = name
        self.phone = phone
        self.address = address
        self.whome_to_meet = whome_to_meet
        self.purpose = purpose
        
        # Automatically pickup the date time stamp
        self.date_time_stamp = datetime.datetime.now()
    
    def visitor_details(self):
        self.name = input('Enter your name:')
        self.phone = input('Enter your phone:')
        self.address = input('Enter your address:')
        self.whome_to_meet = input('Enter your whome_to_meet:')
        self.purpose = input('Enter your purpose:')


    def __str__(self):

        # This fun returns csv string
        # Format of excel Basically
        return '{},{},{},{},{}\n'.format(self.serial_no, self.name, self.phone, self.address, self.whome_to_meet, self.purpose)
        

        

 