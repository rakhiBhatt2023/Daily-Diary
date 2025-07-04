# whatsapp chat visualization
# messages  are a list
# one message is a dictionary bexause it has status of seen , delivered

#chats is a dictionary bigger
Chats={
    'description':'THIS IS THE CHAT BETWEEN AKSHITA AND RAKHI',

     # messages is a list of dictionary

    'messages':[
    {
    'Sender':'Akshita',            
    "Message":"HI , HOW ARE U .",
    'Date':' 12/06/2025',
   'delivered': '9:30',
   'seen':'9:50',    # COLON IS NOT A NUMBER SO PYTHON TREATS IT AS DIVISION OPERATOR IF NOT ' '  ARE THERE
   },

    {
    'Sender':'Rakhi',
    'Message':'HI , I AM FINE',
    'Date': '12/06/2025',
   'delivered': '9:51',
   'seen': '9:58',
    },

    {
    'Sender':'Akshita',
    'Message':'ARE U COMING TODAY ?',
    'Date':' 12/06/2025',
   'delivered': '9:59',
   'seen':'10:00',
    },

    {
    'Sender':'Rakhi',
    'Message':"YES,I'LL BE THERE ON TIME.",
    'Date': '12/06/2025',
   'delivered': '10:00',
   'seen':'10:10',
   },
   
    {
    'Sender':'Akshita',
    'Message':'GREAT.',
    'Date':' 12/06/2025',
   'delivered': '10:12',
   'seen':'10:15',
    },
    ]
}

print(Chats['description'])
print(Chats['messages'])

print("starting chat is at:")
print(Chats['messages'][0]['seen'])

print("Chat ended at:")
print(Chats['messages'][4]['seen'])




