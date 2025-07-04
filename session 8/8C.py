# Problem statement:find max from list of nombers 
# small problem : if only one element
# next small : two elements
def get_max(data,length):

    # Base case
    if length==1: 
        return data[0]
    else:
        previous = get_max(data,length-1) #recursion
        current = data [length-1]   

        if previous > current:
            return previous
        else:
            return current 

numbers=[10,20 ,30]
max_in_numbers = get_max(data = numbers , length = len(numbers))
print('max in numbers=',max_in_numbers)

# write program to fetch min in 5 numbers
# HW draw stack heap 