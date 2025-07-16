from task2_1 import flight                 #  SORTING REMAINING

# OPERATIONS 
def search(flights, fare):
        flag  = False
        index = 0
        while index < len(flights):
            if flights[index].fare == fare:
               flag = True
            index +=1

        if flag == True:
                print('found')
        else:
                print('Not found')

def sort(flights, key):
    for outer in range(len(flights) - 1):
        for inner in range(len(flights) - outer - 1):
            if key == 'fare' and flights[inner].fare > flights[inner + 1].fare:
                flights[inner], flights[inner + 1] = flights[inner + 1], flights[inner]

    for f in flights:
        f.show(flights)

def filter(flights, departure, arrival):
        flag  = False
        index = 0
        while index < len(flights):
            if flights[index].departure == departure and flights[index].arrival == arrival:
                   flights[index].show(flights)

                   flag = True
            index +=1


# objects
flight1 = flight(carrier = 'indigo',flight_code= '6e642',source =  'chandigarh',destination = 'mumbai',departure = '05:50',arrival =  '08:20',duration =  2.3,fare =  6499)
flight2 = flight(carrier = 'air india',flight_code =  'ai2660',source =  'chandigarh',destination = 'mumbai',departure = '17:50',arrival =  '20:45',duration =  2.5,fare =  7260)
flight3 = flight(carrier =  'indigo',flight_code =  '6e5234',source = 'chandigarh',destination = 'mumbai',departure = '16:30',arrival = '19:05',duration =  2.3,fare = 7649)

# List of objects
flights = [flight1,flight2,flight3]
user = input('enter the opertion u want to perform :')

# USER REQUIREMENT
if user == "search":
    fare = int(input('ENTER FARE TO SEARCH:'))
    search(flights,fare)

elif user == "sort":
    key = ('enter the key to sort:')
    sort(flights,key)

elif user == "filter":
    key1 = input('Enter the key to search (departure):')
    key2 = input('Eter value through which you want to search(arrival):')
    filter(flights,key1,key2)

else:
    print("Invalid operation.")



        


