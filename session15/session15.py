def add_in_front(self,car):
    car.next = self.head
    self.head.previous = car
    car.previous = self.tail
    self.size += 1

def add_in_between(self,car1,car2,car):      # caris the new cra to be added
    car1.next = car
    car2.previous = car
    self.size += 1

