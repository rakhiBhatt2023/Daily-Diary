# Daily Expense tracker

expenses = [200, 450, 120, 600, 310, 90, 500]
total=0
for index in range(0,len(expenses)):
    total += expenses[index]
avg = total/len(expenses)
print('Total expense in the week is:',total)
print('Average of expense is:',avg)



