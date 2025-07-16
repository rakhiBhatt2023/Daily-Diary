# List of dictionary objects

flight1 = {
    'carrier': 'air india',
    'flight_code': 'ai522',
    'from': 'chandigarh',
    'to': 'bengaluru',
    'departure': '16:30',
    'arrival': '19:30',
    'duration': 3.0,
    'fare': 6606

}
flight2 = {
    'carrier': 'indigo',
    'flight_code': '6e642',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '05:50',
    'arrival': '08:20',
    'duration': 2.3,
    'fare': 6499
} 
flight3 = {
     'carrier': 'air india',
    'flight_code': 'ai2660',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '17:50',
    'arrival': '20:45',
    'duration': 2.5,
    'fare': 7260
}
flight4 = {
    'carrier': 'indigo',
    'flight_code': '6e5234',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '16:30',
    'arrival': '19:05',
    'duration': 2.3,
    'fare': 7649
}
flight5 = {
    'carrier': 'indigo',
    'flight_code': '6e6634',
    'from': 'chandigarh',
    'to': 'bengaluru',
    'departure': '08:25',
    'arrival': '11:30',
    'duration': 3.5,
    'fare': 6867

}

flights = [flight1, flight2, flight3, flight4, flight5]

for outer in range (0,len(flights)-1 ):
    for inner in range(0,len(flights)-outer-1):
        if flights[inner]['fare'] > flights[inner+1]['fare']:
            temp= flights[inner]
            flights[inner] = flights[inner+1]
            flights[inner+1] = temp


print('flights sorted according to fare : ')
for index in range(len(flights)):
    print(flights[index])




