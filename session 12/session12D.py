# List of Objects
# from and to are keywords so we Can't use them as attributes

""" 
    flight object : Carrier, flight_code, source, destination, departure, arrivval, duration, fare


"""
class Flight:
    def __init__(self,carrier, flight_code, source, destination, departure, arrival, duration, fare):
        self.carrier = carrier
        self.flight_code = flight_code
        self.source = source
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.duration= duration
        self.fare = fare

    def show(self):
        print('___________',self.flight_code,'____________-')
        print('carrier:',self.carrier)
        print('arrival:',self.arrival)
        print('departure:',self.departure)
        print('destination:',self.destination)
        print('duration',self.duration)
        print('fare:\u20b9',self.fare)

