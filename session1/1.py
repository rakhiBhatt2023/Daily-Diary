# Create StatementMore actions
# MODEL: Container -> Single Value
num1 = 10
# num1: is a reference variable created in STACK of RAM     #num1 STACK mein reference store karta hai.
# 10 gets strored in a Container of type int in HEAP of RAM    #value heap me store hoti h

# Read Statement
print('num1 is:', num1)
print('type of num1 is:', type(num1))  
print('num1 hashcode is:', id(num1))  #unique memory id (HEAP KA ADDRESS)

# Update Statement
num1 = 20

# Read Statement -> VIEW
print('num1 now is:', num1)
print('type of num1 now is:', type(num1))
print('num1 hashcode now is:', id(num1))  #uniques address of 20

# Delete Statement
# Explicit (del statement) or Implicit (Automatic)
del num1   #num 1 ref ko STACK se hata diya gaya

print('num1 now is:', num1)
print('type of num1 now is:', type(num1))
print('num1 hashcode now is:', id(num1))