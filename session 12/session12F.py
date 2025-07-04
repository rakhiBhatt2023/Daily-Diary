from session12E import Flightlist
from session12D import Flight

flight1 = Flight(carrier ='indigo',flight_code='6E542',source = 'chandigarh',arrival = '1:05' , destination = 'mumbai',departure = '17.50',duration=2.6,fare= 8760)

flight2 = Flight(carrier =  'air india',flight_code = 'ai2660',source='chandigarh',
                 destination= 'mumbai',departure = '17:50', arrival =  '20:45',duration= 2.5,fare =  7260)

flight3 = Flight(carrier = 'indigo',flight_code =  '6e5234', source = 'chandigarh',
                 destination='mumbai',departure =  '16:30',arrival = '19:05',duration = 2.3,fare =  7649)

flight4 = Flight(carrier = 'air india',flight_code = 'ai522',source =  'chandigarh',
           destination = 'bengaluru',departure = '16:30',arrival =  '19:30',
           duration = 3.0,fare = 6606)

flight5 = Flight(carrier = 'indigo',flight_code = '6e6634',source =  'chandigarh',
          destination = 'bengaluru',departure =  '08:25',arrival = '11:30',
          duration = 3.5,fare =  6867)



flights = Flightlist()   # Object og flightlist

flights.add(flight1)
flights.add(flight2)
flights.add(flight3)
flights.add(flight4)
flights.add(flight5)


flights.iterate()

flights.search(flightcode='66e34')


