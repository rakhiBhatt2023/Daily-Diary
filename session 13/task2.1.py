class flight:
    def __init__(self,carrier,flight_code,source,destination,fare):
        self.carrier  = carrier
        self.flight_code = flight_code
        self.source = source
        self.destination = destination
        self.fare = fare


    def show(self):
        print('___________FLIGHT___________')
        print('carrier:',self.carrier)
        print('flight code:',self.flight_code)
        print('source:',self.source)
        print('destination:',self.destination)
        print('Fare:',self.fare)

        


