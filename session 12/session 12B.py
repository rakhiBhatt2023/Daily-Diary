# Make my trip example searching 

flight1={
    'carrier':'indigo',
    'flight_code':'6E542',
    'from':'chandigarh',
    'to':'mumbai',
    'daparture':'17.50',


}
flight2 = {
    'carrier': 'air india',
    'flight_code': 'ai2660',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '17:50',
    'arrival': '20:45',
    'duration': 2.5,
    'fare': 7260
}

flight3 = {
    'carrier': 'indigo',
    'flight_code': '6e5234',
    'from': 'chandigarh',
    'to': 'mumbai',
    'departure': '16:30',
    'arrival': '19:05',
    'duration': 2.3,
    'fare': 7649
}

flight4 = {
    'carrier': 'air india',
    'flight_code': 'ai522',
    'from': 'chandigarh',
    'to': 'bengaluru',
    'departure': '16:30',
    'arrival': '19:30',
    'duration': 3.0,
    'fare': 6606
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

# List of Dictionary 
flights = [flight1, flight2, flight3, flight4, flight5]

# Use Linear Search, to search flights from chandigarh to mumbai or begaluru

# Filter Says: Search all of the data/elements matching criteria

# use linear search to search flights from chandigarh to maumbai or bangaluru  is FILTERING
# filter says: search for all objects but
# search :for one object
# source =input('Enter your source:')
# destination = input('Enter your destination:')


# This is filtering
for index in range(len(flights)):
    if flights[index]['from'] == source and flights[index]['to'] == destination:
        print(flights[index])
    
     


# using linear search on flight code
code = input('enter flight code:')

flag = False
for index in range(0, len(flights)):
    if flights[index]['flight_code'] == code:
        flag = True

    else:
        flag = False

if flag == True:
    print(flights[index])

else:
    print('flight not found')

