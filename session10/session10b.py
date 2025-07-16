class Restaurant:
    
    def __init__ (self, name='NA', phone = 'NA',email = 'NA', rating = 0, price_per_person= 0, menu = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.rating = rating
        self.price_per_person = price_per_person
        self.menu = menu

    def show(self):
            print("------------------------------")
            print("^^^^^^^^^^^RESTURANT^^^^^^^^^^^^")


            print("Name:", self.name)
            print("Phone:", self.phone)
            print("Email:", self.email)
            print("Rating:", self.rating)
            print("Price_per_person:", self.price_per_person)
            print("Menu:", self.menu)
            print("------------------------------")

            #print("menu:",self.menu)

            print("Menu")
            self.menu.show()
            print("^^^^^^^^^^^RESTURANT^^^^^^^^^^^^")


            # There are no objects in this therefore print ni ho raha h


    

        
        