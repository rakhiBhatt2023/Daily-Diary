def square(number):
    result= number*number
    return result

print('square now is:',square)

# print('sqaure is:',square)
# print('type of sq is:',type(square))
# print('hashcode of sq:',id(square))


def square(number1,number2):
    result = number1*number2
    return result

print('square now is:',square)

# print(square(10))        this throws an error because it will be removed and newone will created 
                     # error is that second parameter is missing

result_from_square = (square(10,20))  #200
print('result is:',result_from_square)