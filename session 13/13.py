"""
    sorting 

    BUBBLE SORT
"""

Numbers = [10,30,50,20,40]     # len(Numbers) = 5 becoz 5 elements    

# Nested Loops
for outer in range(0,len(Numbers)-1):

    for inner in range(0,len(Numbers)-outer-1):

        if Numbers[inner] >Numbers[inner+1]:
            temp = Numbers[inner]
            Numbers [inner] = Numbers[inner+1]
            Numbers[inner+1] = temp

print('Sorted numbers are:',Numbers)


"""
numbers: [10, 30, 50, 20, 40]

outer  : 0, 1, 2, 3
outer  : 0
numbers: 10, 30, 50, 20, 40
----------
inner  : 5-0-1 -> 4, 0 to 3
inner  : 0, 10 > 30 ?
         10, 30, 50, 20, 40
inner  : 1, 30 > 50 ?
         10, 30, 50, 20, 40
inner  : 2, 50 > 20 ?
         10, 30, 20, 50, 40
inner  : 3, 50 > 40 ?
         10, 30, 20, 40, 50

----------
outer  : 1
numbers: 10, 30, 20, 40, 50
-----------
inner  : 5-1-1 ->3   ,0 to 2
inner  : 0 , 10 > 30
         10 30 20 40 50 
inner  :  1, 30 > 20
          10 20 30 40 50
inner   : 2, 20 > 40
          10 20 30 40 50
-----------
outer   : 2
numbers  : 10 20 30 40 50
inner    : 5-2-1  -> 2  ,0 to 1
inner    : 0 , 10 > 20
          10 20 30 40 50
inner    : 1, 20 > 30 
          10 20 30 40 50
-----------
outer : 3
numbers: 10 20 30 40 50
inner  :5-3-1  -> 1 ,  0
inner  :0  , 10 > 20
       10 20 30 40 50







    

"""
