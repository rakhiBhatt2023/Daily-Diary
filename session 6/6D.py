numbers = [10, 17, 23, 45, 9, 12]                              #45
ipl_scores = [111, 210, 120, 97, 56, 32]                        #210
product_prices = [100, 50, 77, 80, 12, 99, 20, 200, 76, 55]     #200

max_number = numbers[0]
for index in range (0,len(numbers)):
    if numbers[index] > max_number:
        max_number = numbers[index]
        print('Max number is:',numbers[index],'at index',index)

print('_______________')

max_number = ipl_scores[0]
for index in range (0,len(ipl_scores)):
    if ipl_scores[index] > max_number:
        max_number = ipl_scores[index]
        print('Max number is:',ipl_scores[index],'at index',index)
        
print('_______________')


max_number = product_prices[0]
for index in range (0,len(product_prices)):
    if product_prices[index] > max_number:
        max_number = product_prices[index]
        print('Max number is:',product_prices[index],'at index',index)

