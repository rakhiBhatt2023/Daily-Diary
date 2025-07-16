class flight:
    def __init__(self,carrier,flight_code,source,destination,duration,departure,arrival,fare):
        self.carrier  = carrier
        self.flight_code = flight_code
        self.source = source
        self.destination = destination
        self.fare = fare
        self.departure = departure
        self.arrival = arrival
        self.duration = duration


    def show(self,flights):
        print('___________FLIGHT___________')
        print('carrier:',self.carrier)
        print('flight code:',self.flight_code)
        print('source:',self.source)
        print('destination:',self.destination)
        print('Fare:',self.fare)
        print('departure:',self.departure)
        print('arrival:',self.arrival)
        print('duration:',self.duration)

