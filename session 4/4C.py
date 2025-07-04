flight_booking={
    'from': input('Enter from location:'),
    'to': input('Enter to location:'),
    'travellers': int(input('Enter no of travellers:')),
    'feedback': float(input('Enter feedback at scale of(0-5):')),
}
print(flight_booking, type(flight_booking))
print(flight_booking['from'],type('from'))
