coupon_code = input("Enter your coupon code:")
Billing_amount = int(input("Enter your billing ammount:"))

# Nested if - else

# if(coupon_code=='NOMNOW150'):
#     print('Copon available')
#     if(Billing_amount > 449):
#         Billing_amount -= 150
#         print('Total bill to pay is:',Billing_amount)
#     else:
#         print('Sorry your coupon is not available')
#         print('Please add items worth',(450-Billing_amount),'to apply your coupon')
# else:
#     print('coupon invalid. Please check and apply again')

#    using and instead of if ladder.used in signin form either pass or username is incorrect 

if coupon_code == 'NOMNOW150' and Billing_amount > 449:
    print('coupon can be applied')
    Billing_amount -= 150 # billing_amount = billing_amount - 150
    print('please pay:', Billing_amount)
    print('thank you')
else:
    print('either coupon or billing amount is failing')
