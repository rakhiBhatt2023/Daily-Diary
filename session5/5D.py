# Linear search algorithm
# while loop

username=['john', 'jennie', 'fionna', 'kia', 'leo']
search = input('Enter username to search: ')

index=0
flag = False
while index < 5:
    if username[index] == search:
        print('username found at index:',index)
        flag = True
        break   #for getting out of if statement

    else:                                # you can skip else if want 
        print('username not found')     

    index += 1 #update statement
if flag == False:
    print('user not found')

    
              