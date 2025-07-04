# Searching using function
# Time complexity =  o(n)

def search(data=[],element = None):

    flag = False
    for index in range(0,len(data)):
       if data[index] == element:
           print(element,"found at index:",index)
           flag =True
           break

    if flag == False:
       print('element not found')

numbers = [10,20,30,40,50]
names = ['john','jennie','sia','kim']

search(numbers,int(input('Enter a number to search:')))
search(names,'ben')