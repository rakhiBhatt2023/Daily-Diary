# HW: Create a function, which takes input a list and returns a list of reverse numbers
# HW: Create a function, which takes input a list and reverse numbers in the same list



def user_input():
    your_List = list(input('Enter your list:'))
    reverse_list = list(reversed(your_List)) 
    print('Reversed list is:',reverse_list)

numbers = user_input()
