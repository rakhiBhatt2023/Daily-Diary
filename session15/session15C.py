class Product:
    def __init__(self,name,price,quantity,brand):
        self.name = name
        self.price = price 
        self.quantity = quantity
        self.brand = brand
        self.next = None
        self.previous = None

    def show(self):
        print('________PRODUCT_______')
        print('Name:',self.name)
        print('Price:',self.price)
        print('Quantity',self.quantity)
        print('Brand:',self.brand)
        print('__________________')



class Shopping_cart:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size  = 0

    def add(self,product):
        self.size += 1

        if self.head == None:
            self.head = product
            self.tail = product
        else:
            self.tail.next = product
            self.tail = product
            product.next = self.head
            product.previous = self.tail 
            self.head.previous = product

    def iterate(self):
        product = self.head
        product.show()
        while product.next != self.head:
            product = product.next
            product.show()
    

    def update(self):
        product_name = input(('Enter your product name to update:'))
        current = self.head
        while True:
            if current.name == product_name:
                if current.quantity == 0:
                    self.remove_product(current)
                else:
                    current.quantity -= 1
                return
            current = current.next
            if current == self.head:
               break
            

    def remove_product(self, product): 
        # In this function no need to iterate to find object becoz we are already at that node where that updated product is available      
        if self.head == self.tail == product:
            self.head = self.tail = None

        elif product == self.head: 
 #          to remove first node if mathed
            self.head = self.head.next
            self.head.next = self.tail
            self.tail.next = self.head 

        elif product == self.tail:
#           to remove tail last node
            self.tail = self.tail.previous
            self.tail.next = self.head
            self.head.previous = self.tail

        else:
             product.previous.next = product.next
             product.next.previous = product.previous

        self.size -= 1


            
            
            
 
           
