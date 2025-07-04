"""
   Object     | attributes i.e. data associated with object 
   -------------------------------------------------------
   Restaurant | name, phone, email, address, rating, priceperperson, menu
   Menu       | name, dishes, numberofdishes
   Dish       | name, price, rating

   1 restaurant has 1 menu
    1 menu has many dishes


 """

class Menu:

    # Dishes in menu can be more than 1 therfore list initialized

    def __init__(self, name = 'NA', dishes = [] , number_of_dishes = 0):
        self.name = name
        self.dishes = dishes
        self.number_of_dishes = number_of_dishes

    def show(self):
        print("------------------------------")
        print("~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~")
        print('Name:',self.name)
        print('dishes:',self.dishes)



        print("Dishes:")
        for index in range(len(self.dishes)):
            self.dishes[index].show()                            # session 10 wala show() fun call ho raha h
        print("number_of_dishes:", self.number_of_dishes)         # will print 3 as dishes are 3 in 10c.py
        


        print("------------------------------")
        print("~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~")

        # There are no objects in this therefore print ni ho raha h

        

