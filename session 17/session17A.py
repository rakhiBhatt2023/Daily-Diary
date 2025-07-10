# explore dic data structure

my_data = {
    101: 'John',
    201: 'Jennie',
    501: 'Sia',
    99: 'Joe',
    25: 'Kim',
    201: 'Anna',
    21: 'Joe',
}

print('my_data',my_data)

print('len(my_data)',len(my_data))
print('Max of my_data:',max(my_data))
print('Min of my_data:',min(my_data))
# print('sum of my_data:',sum(my_data))     # It will work on numbers only not on string


# value = my_data[101]
value = my_data.get(101)
print('Value:',value)

# Update
my_data[101] = 'Joseph'
print(my_data)

# Delete
my_data.pop(25)
# del my_data(25)
print('my data after pop:')
print(my_data)

# add a new element
my_data[444] = 'Anna'
print(my_data)

