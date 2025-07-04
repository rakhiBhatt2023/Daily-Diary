class Chat:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self,message):
        self.size += 1

        if  self.head == None:
            self.head = message
            self.tail = message
        else:
            self.tail.next = message
            message.previous = self.tail      
            message.next = None
            self.tail = message

    def iterate(self, directoin=0):
        if directoin == 0:
            message = self.head
            while message:
                message.show()
                message = message.next
        else:
            message = self.tail
            while message:
                message.show()
                message = message.previous