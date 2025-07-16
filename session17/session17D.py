months_list = ['jan','feb','March','April','May','June','july',
               'August','September','October','november','December']


College_attendance = {}.fromkeys(months_list,100)
print('College attendance:')
print(College_attendance)

# Students
students = {
    101: 'John',
    201: 'Jennie',
    501: 'Sia',
    99: 'Joe',
    25: 'Kim',
    201: 'Anna',
    21: 'Joe',
}
keys = list(students.keys())                    # Students se keys nikal di like roll no (dictionary)
attendance = {}.fromkeys(months_list,100)        # dict of attendance with months

attendance_record = {}.fromkeys(keys,attendance)
# attendance_record = {}.fromkeys(list(students.keys()), 
#                                 {}.fromkeys(months_list, 100))
print('attendance_record')
print(attendance_record)

attendance_record[101]['jan']  -= 5
print(attendance_record)

