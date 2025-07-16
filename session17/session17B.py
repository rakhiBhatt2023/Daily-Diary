
# list of dictionary
months_list = ['jan','feb','March','April','May','June','july',
               'August','September','October','november','December']

College_attendance = {}.fromkeys(months_list,100)

print('College attendance:')
print(College_attendance)

College_attendance['jan'] -= 5

print('College attendance:')
print(College_attendance)





