from_location=input("Enter from location:")
print("You entered locatoin:",from_location)
print(type(from_location))

to=input("Enter destination:")
print("You entered destination:",to)
print(type(to))

No_of_travellers=int(input("Enter no of travellers:"))

# one_way_flight_booking={}
# one_way_flight_booking['from']=from_location
# one_way_flight_booking['to']=to
# one_way_flight_booking['travellers']=No_of_travellers


one_way_flight_booking={

    'from':from_location,
    'to':to,
    'travellers':No_of_travellers
}

print('your travellers are:',one_way_flight_booking['travellers'])
print(type(one_way_flight_booking['travellers']))