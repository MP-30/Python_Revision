"""
stock_prices = [298, 305, 320, 301, 292]

for i in range(len(stock_prices)):
    if stock_prices[i] == 301:
        print (i)
        
""" 
"""    
# Lets us say expense for every month are listed below,
1. January - 2200
2. February - 2350
3. March - 2600
4. April - 2130
5. May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
"""
month_expenses = [2200, 2350, 2600, 2130, 2190]

extra_expenses_feb = month_expenses[1] - month_expenses[0]
print(extra_expenses_feb)
total_expense_quarter = month_expenses[0] + month_expenses[1] + month_expenses[2]
print(total_expense_quarter)
for i in month_expenses:
    if i == 2000:
        print (True)
else: print (False)
june = 1980
month_expenses.append(june)
print(month_expenses)
month_expenses[3] = 1930
print(month_expenses)


'''
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

'''

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
heros.remove('black panther')
hulk_place = heros.index('hulk')
heros.insert(hulk_place+1, 'black panther')
heros[1:3] = ['doctor strange']
heros.sort()
print(heros)

'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

max_num = 56
odds = []
for i in range(0,max_num):
    if i %2 != 0:
        odds.append(i)
print(odds)