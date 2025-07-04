names = ["john", "jennie", "jim"]
followers = names

print('names:')
print(names, type(names), id(names))
print('followers:')
print(followers, type(followers), id(followers))

names[1] = 'george'
names = ['leo', 'george', 'ben']     #this is new list now  so have new address


print('names now:')
print(names, type(names), id(names))
print('followers now:')
print(followers, type(followers), id(followers))    #i have again not done followers = names so followers value is still same above


print(names[1], type(names[1]), id(names[1]))            #george is previously in the stack so new list will point to that address
                                                            #that is why george have same hash id
print(followers[1], type(followers[1]), id(followers[1]))