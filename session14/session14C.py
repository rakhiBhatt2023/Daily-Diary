class CarList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add is going to add a car in the linked list
    def add(self, car):
        self.size += 1

        if self.head == None:
            self.head = car
            self.tail = car
        else:
            self.tail.next = car
            car.previous = self.tail
            car.next = self.head
            self.head.previous = car
            self.tail = car

    def iterate(self, direction=0):

        if direction == 0:
            car = self.head
            print(car)
            while car.next != self.head:
                car = car.next
                print(car)
        else:
            car = self.tail
            print(car)
            while car.previous != self.tail:
                car = car.previous
                print(car)


    def delete(self, car):
        self.head.next = car.next
        self.tail.previous = car.previous            # This is also correct but actual coorrect code is in session 15
        print(car)

    def delete_head(self):
        if self.head  == None:
            print('Nothing is there to delete')
        elif self.head==self.tail:
            self.head = self.tail = None
            self.size = 0
        else:
            self.tail.next = self.head.next
            self.head = self.head.next
            self.head.previous = self.tail
            self.size -= 1


    def delete_tail(self):
        self

    def bubble_sort(self):
        pass