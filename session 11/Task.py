# doubly linked list

class messages:
    def __init__(self, text, sender, reciever, status):
        self.text = text
        self.sender = sender
        self.reciever = reciever
        self.status = status
        self.previous = None
        self.next = None

    def show(self):
        print('____________Message___________')
        print('Text :',self.text)
        print('sender:',self.sender)
        print('reciever:',self.reciever)
        print('Status:',self.status)
        print('_______________________________')

    
        

        
        