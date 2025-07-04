data=8
key=3

# right shift          
encrypted=data>>key     # data divide by 2 power key i.e. 8/2 raise power 3
print("Encrypted data is:",encrypted)

# left shift
original =data<<key   #data multiply by 2 power key i.e.8*2 raise power 3
print("original data is:",original)