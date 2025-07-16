# 1..count how much time you spend 500

expenses = [200, 500, 120, 500, 310, 90, 500]
count = 0
for index in range(len(expenses)):
    if expenses[index] == 500:
        count += 1

print('count is:',count)



# 2.. Print only the items that cost less than ₹100 from the cart:
cart_prices = [120, 250, 60, 90, 150]
for index in range(len(cart_prices)):
    if cart_prices[index] < 100:
        print('less than 10 is:',cart_prices[index])


# 3.. ATM pin entry The user is allowed up to 3 attempts to enter the correct 4-digit PIN (e.g., 1234). If they enter the correct PIN within 3 tries, print "Access granted". If not, print "Account locked".

correct_pin=1234

attempts=0
while attempts < 3:
    pin = int(input('Enter your pin:'))

    if pin == correct_pin:
        print('Access granted')
        break
    else:
        print('Try again')

    attempts += 1
if attempts == 3:
    print('Account locked')





