def get_min(data , length):
    if length == 1:
        return data[0]
    else:
        previous = get_min(data,length-1)
        current = data[length-1]
        if previous < current:
            return previous
        else:
            return current


numbers = (50,30,40,20,10)
min_number = get_min(numbers,len(numbers))
print('Minimum numbers is:',min_number)
