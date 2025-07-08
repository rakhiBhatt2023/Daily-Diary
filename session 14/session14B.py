class Car:
    def __init__(self,name,brand,price,range,hp):
        self.name = name
        self.brand = brand
        self.price = price
        self.range = range
        self.hp = hp

        # internal usage to create linked list
        self.previous = None
        self.next = None
    
    def user_inputs(self):
        self.name = input("Enter Car name:")
        self.brand = input('Enter brand name')
        self.price = int(input("Enter Car price:"))
        self.range = int(input("Enter Car range:"))
        self.hp = input("Enter Car horse power:")

# replacemnet of show function
# String Function
# # to show the data of object
# you can directly print reference variable, which will 
# automatically execute string function
    def __str__(self):

        car_string = """
~~~~~~~~~~~~~{}~~~~~~~~~~~~~
Brand: {}
Price: {}
Range: {}
HP: {}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""".format(self.name, self.brand, self.price, self.range, self.hp)

        return car_string