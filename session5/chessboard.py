black_square = '\u25A0'
white_square= '\u25A1'

for row in range(0,8):
    for col in range(0,4):
        if(row%2==0):
             print(white_square,end =' ')
             print(black_square,end =' ')
        else:
             print(black_square,end =' ')
             print(white_square,end =' ')
       
    print()