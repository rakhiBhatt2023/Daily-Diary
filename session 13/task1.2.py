from  task import flight
from task1 import flightlist

flight1 = flight(carrier = 'air india',
                 flight_code = '6e340',
                source = 'Ludhiana',
                destinition = 'Chennai',
                fare = 6685)

flight2 = flight(carrier='air india',
    flight_code='ai522',
    source='chandigarh',
    destinition='bengaluru',
    fare=6606)

flight3 =  flight(
    carrier='indigo',
    flight_code='6e6634',
    source='chandigarh',
    destinition='bengaluru',
    fare=6867)

flight4 = flight(carrier='indigo',
    flight_code='6e5234',
    source='chandigarh',
    destinition='mumbai',
    fare=7649)


flights = flightlist()
flights.add(flight1)
flights.add(flight2)
flights.add(flight3)
flights.add(flight4)

flights.sort_by_fare(flights)