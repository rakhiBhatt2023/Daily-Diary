
def square_of_number(numbers):
    print('numbers is:',numbers , id(numbers) , type(numbers))
    for index in range(len(numbers)):
        print(' numbers is:',numbers[index],id(numbers[index]), type(numbers[index]))   # hashcode of numbers is same as data   -> refernce copy operations
    
    for index in range(len(numbers)):
        numbers = numbers * numbers
        print('[square of no] is:',numbers[index],type(numbers[index]),id(numbers[index]))    


data = [10, 20,30,40,50]
print('[main]',data,id(data),type(data))

for index in range(len(data)):
    print('[main:]',data[index],type(data[index]),id(data(index)))
    
square_of_number(data)

print('-----------------')
print('[main] data now is:',data,id(data), type(data))

for index in range(len(data)):
    print('[main]',data[index] , type(data[index] , id(data[index])))
