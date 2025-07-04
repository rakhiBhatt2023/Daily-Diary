"""
    Searching 
    liners search 
     1. simple list
     2.list of dictionary
    3. list of objetcs
    4. our linked list
"""
data = [10,20,30,40,50]                            
number = int(input('Enter number to search:'))

flag = False
for index in range(0,len(data)):
    if data[index] == number:
        print("Number found at index:",index)
        flag =True
        break

   

if flag == False:
    print('number not found')



# for names
names = ['john','jennie','anna','kim','ben']
name = input('Enter name to search:')
index = 0
found = False

while index < len(names):
    if names[index] == name:
        found =True
        break
    else:
        found = False

    index += 1

if found == False:
    print('Name not found')
else:
    print('name found at index',index)




