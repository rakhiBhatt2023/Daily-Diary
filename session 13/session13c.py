# list of objects 
# sorting using oops 
class flights:
    def __init__(self, carrier, flight_code, source, destination, arrival, duration, fare):
        self.carrier = carrier
        self.flight_code = flight_code
        self.source = source
        self.destination = destination
        self.arrival = arrival
        self.duration = duration
        self.fare = fare
    
    def show(self):
        print('_________FLIGHTS__________')
        print('carrier:',self.carrier)
        print('flight_code:',self.flight_code)
        print('source:',self.source)
        print('destination:',self.destination)
        print('arrival:',self.arrival)
        print('duration:',self.duration)
        print('Fare:',self.fare)

    


flight1 = flights('indigo','6e6634','Bengaluru','Chandigarh','11:30', 3.5, 6867)
flight2 = flights(carrier = 'AIR INDIA', flight_code = 'ai522', source = 'Chandigarh', destination = 'Bengaluru', arrival = '19:30', duration = 2.3, fare = 6606)
flight3 = flights(
    carrier  = 'air india',
    flight_code = 'ai2660',
    source= 'chandigarh',
    destination ='mumbai',
    arrival =  '20:45',
    duration = 2.5,
    fare  = 7260)

flightlist = [flight1, flight2, flight3]

# flight1.show()

for outer in range (0,len(flightlist)-1 ):
    for inner in range(0,len(flightlist)-outer-1):
        if flightlist[inner].fare > flightlist[inner+1].fare:
            temp = flightlist[inner]
            flightlist[inner] = flightlist[inner+1]
            flightlist[inner+1] = temp


print('flights sorted according to fare : ')
for index in range(len(flightlist)):
    print(flightlist[index].show())


