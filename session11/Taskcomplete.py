from Task import messages
from Task1 import Chat

message1= messages(text ='1.Hey Priya! Did you reach home safely?',
                   sender = 'Rahul',reciever= 'Priya',status = 'Seen',)

message2 =messages(text = '2.Heyy! Yes, just got in. Thanks for checking 😊',sender='Priya',
                    reciever='Rahul',status = 'Delivered')

message3 = messages(text ='3.Great Then',sender = 'Rahul',reciever='Priya',status='seen')

chats = Chat()  # object of chat

chats.add(message = message1)
chats.add(message = message2)
chats.add(message = message3)


print('Backward:')
chats.iterate(directoin=1)     # prints reverse 
print('forward:')
chats.iterate()
