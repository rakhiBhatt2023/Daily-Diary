"""
   zomato :20% off
   min amount = 300


   bingo : 50% off
   min amount = 500
   min discount = 150

"""

promo_code = input('Enter your promo code:')
amount = float(input('Enter your amount:'))

# Ladder if-else

if promo_code =='zomato':
    if amount > 300:
       discount = 0.2 * amount
       amount_to_pay = amount - discount
       print('total amount to pay is:',amount_to_pay)


    else:
       print('coupon cannot be applied')
       print('You have to pay:',amount)
       print('or u can add items worth','\u20b9',(301-amount),'to apply coupon code')

elif promo_code == 'bingo':
   if amount > 500:
      discount = 0.5 * amount
      if amount > 500:
        discount = 0.50 * amount
        if discount > 150:
            discount = 150
        bill_to_pay = amount - discount
        print('You got a discount of \u20b9', discount)
        print('Your amount was \u20b9', amount)
        print('Please pay: \u20b9', bill_to_pay)
   else:
        print('Please add items worth', (501-amount), 'more to get discount')
else:
    print('Invalid Coupon Code')