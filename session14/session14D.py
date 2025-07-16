from session14B import Car
from session14C import CarList

list = CarList() # head, tail and size

car1 = Car(name='Harrier EV', brand='Tata', price=3000000, range=450, hp='200 HP')
car2 = Car(name='Be6', brand='BYD', price=2800000, range=400, hp='180 HP')
car3 = Car(name='Windsor EV', brand='MG', price=3200000, range=470, hp='220 HP')


# print('car1 hashcode:', id(car1))
# print('car2 hashcode:', id(car2))
# print('car3 hashcode:', id(car3))

list.add(car=car1)
# list.add(car=car2)
# list.add(car=car3)

# print('list head hashcode:', id(list.head))
# print('list tail hashcode:', id(list.tail))

# print('car1 next hashcode:', id(car1.next))
# print('car1 previous hashcode:', id(car1.previous))

# print('car2 next hashcode:', id(car2.next))
# print('car3 previous hashcode:', id(car2.previous))

# print('car3 next hashcode:', id(car3.next))
# print('car3 previous hashcode:', id(car3.previous))
print('--------Before deltion-----------------')
list.iterate()

# Calling deletion function
# list.delete(car2)
# print('-----------After deletion of car2-----------')
# list.iterate()

# deletion of head node
list.delete_head()
print('-----------After deletion of Head-----------')
list.iterate()

