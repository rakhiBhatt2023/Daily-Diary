#file = open('quotes.txt','w')            # use a to append w will overwrite
file = open('quotes.txt','a')


print('Keep entering quotes.Type quit to break')
quote = input('Enter a quote:')


while quote != 'quit':
    file.write(quote)
    file.write('\n')                        # for adding a new line after quote and before new  quote entering
    print('-------Quote saved-------')
    quote = input('Enter a quote:')
 

"""
file = open('quotes.txt', 'a')
quote = input('Enter a Quote: ')
file.write(quote)
file.write('\n')
"""

