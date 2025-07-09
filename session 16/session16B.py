# Explore set

john_followers = {'fionna', 'Sia','kim','harry', 'George','sia'}
print('John_followers:',john_followers)
print(type(john_followers))
print(len(john_followers))
print(min(john_followers))
print(max(john_followers))
# pop on sets will be dangerous so we wont know what has been remove

numbers = list(range(10,101,10)) 
A = {1,2,3,4,5}
B = {4,5,6,7,8} 

C = A+B                            # Sets donot support concatenation
print(C)

D = A - B                          # it is not actual minus it is A/B
print('D is:',D)

E = A ^ B
print('E is:',E) 

F = A|B
print('F is:',F)

A.clear()
print('A is:',A)                   # Clears the whole set

