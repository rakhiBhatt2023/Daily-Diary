class User:
    def __init__(self,name,emailid,phone,address, gender, age):
        print('constructor executed')
        print('self:', self, type(self), id(self))
        self.name = name
        self.emailid = emailid
        self.phone = phone
        self.address = address
        self.gender = gender
        self.age = age

    def show(self):
        print('Constructor executed')
        print('___________________')
        print(vars(self))

john = User(name='john mark', emailid='john@example.com', phone = '+9026784456', address = 'hometown',gender = 'Male' , age=20)
# fionna = User()
# Jack = User()

john.show()


