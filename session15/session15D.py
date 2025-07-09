from session15C import Product
from session15C import Shopping_cart

# objects created
product1 = Product(name = "Wireless Mouse", price = 25.99, quantity = 0, brand = "Logitech")
product2 = Product("Mechanical Keyboard", 89.99, 50, "Corsair")
product3 = Product("HD Monitor", 199.99, 30, "Dell")
product4 = Product("USB-C Hub", 39.99, 75, "Anker")


products = Shopping_cart()

products.add(product1)
products.add(product2)
products.add(product3)
products.add(product4)

products.iterate()
products.update()
print('afater updation:')
products.iterate()