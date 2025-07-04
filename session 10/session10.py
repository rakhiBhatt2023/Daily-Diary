class Dish:

    # self is the first input, and it holds the hashcode of current object
    def __init__(self, name='NA', price='NA', rating='NA'):
        # RHS name (this is the input which we can pass in the constructor as value)
        self.name = name 
        self.price = price
        self.rating = rating


    # self will always be available as 1st input
    # in all the functions, created inside the class
    def show(self):
        print("___________ DISH_______________")
        print('Name:',self.name)
        print('Price:',self.price)
        print('Ratings:',self.rating)
        print("___________ DISH_______________")

# dish1 = Dish()
# dish2 = Dish(name='panerr Tikka',price = 200 ,rating=4.5)
# dish3 = Dish(name='noodles',price = 100 ,rating=3.5)


# print('dish1:',dish1)
# print('dish2:',dish2)       # calls constructor only dont show the details like name etc. of dishes
# print('dish3:',dish3)


# dish1.show()   # It will show all details regarding dishes
# dish2.show()
# dish3.show()