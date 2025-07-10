class Visitor:
    def __init__(self,name=None,phone=None,purpose=None,meet_to=None):
        self.name = name 
        self.phone = phone
        self.purpose = purpose
        self.meet_to = meet_to

    def add_visitor(self):
        self.name = input('Enter your name:')
        self.phone = input('Enter your phone:')
        self.purpose = input('Enter your purpose:')
        self.meet_to = input('Enter your meet_to:')

    def to_CSV(self):
         # csv = '{},{},{},{}\n'.format(self.name, self.phone, self.purpose, self.meet_to)
        # return csv
              #   or can use this below also  
              
        return '{},{},{},{}\n'.format(self.name,self.phone,self.purpose,self.meet_to)
    



    
