class flightlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def add(self,flight):

        self.size += 1
        if self.head == None:
            self.head = flight
            self.tail = flight

        else:
            self.tail.next = flight
            flight.previous = self.tail
            self.tail = flight
            self.tail.next = None

    def sort_by_fare(self,flights):
        while flights:
           for outer in range(0,len(flights) - 1):
               for inner in range(0,len(flights) - outer - 1):
                   if flights[inner].fare > flights [ inner + 1].fare:
                    
                       
                       temp = flights[inner].fare
                       flights[inner].fare = flights[inner + 1].fare
                       flights[inner+1].fare =  temp
   


        
    
    

