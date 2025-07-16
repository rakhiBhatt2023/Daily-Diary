# Searching on linked list
# circular doubly linked list
class Flightlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self,flight):
        self.size += 1

        if  self.head == None:
            self.head = flight
            self.tail = flight
        else:
            self.tail.next = flight
            flight.previous = self.tail 
            flight.next = self.head     
            self.head.previous = flight
            self.tail = flight

    def iterate(self, directoin=0):
        if directoin == 0:
            flight = self.head
            flight.show()                       # this show wil print head flight becoz inseide loop we have skipped it
            while flight.next != self.head:
                flight = flight.next
                flight.show()
        else:
            flight = self.tail
            flight.show()                        # this show wil print tail flight becoz inseide loop we have skipped it
            while flight.preious != self.tail:
                flight.show()
                flight = flight.previous


    def search(self,flightcode):
        flag = False
        if Flightlist.flight_code == flightcode:
            flag = True
        else:
            flag = False

    if flag == True:
    print('Found')
else:
