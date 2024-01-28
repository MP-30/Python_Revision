'''
mylist  = [1,2,3]
for num in range(0,10,2):
  print(num)
  
print ('***************')

word = 'abcdef'
for index,letter in enumerate(word):
  print(index)
  print(letter)
  print('\n')

print ('***************')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = ['e','r','t','h']
z = zip(mylist1, mylist2, mylist3)
for item in z:
  print(item)
  
print(list(zip(mylist3, mylist1, mylist2)))

print('*******************')
print('x' in [1,2,3,4,5])

print ('a' in 'aditya')

print ('mykey' in {'mykey', 6985})
d = {'mykey': 345}
print(345 in d.values())


print('*******************')
mylist = [10,20,30,40,50,60]
print(min(mylist))
print (max(mylist))


from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)

from random import randint

print(randint(10,1000))

result =  input ('Enter your number')
print(result)
print(type(result))
print("*****************************")
'''
data = [{'owner': 'shrisai@moneybloom.in',
  'item_name': 'WIRING HARNESS FOR SLIC-432 & IC-510',
  'amount': 401.0},
 {'owner': 'blackstone@moneybloom.in',
  'item_name': 'WIRING HARNESS FOR SLIC-432 & IC-510',
  'amount': 500.0},
 {'owner': 'everest@moneybloom.in',
  'item_name': 'WIRING HARNESS FOR SLIC-432 & IC-510',
  'amount': 501.0},
 {'owner': 'shrisai@moneybloom.in',
  'item_name': 'Copper pipe',
  'amount': 532.0},
 {'owner': 'blackstone@moneybloom.in', 'item_name': '456', 'amount': 550.0},
 {'owner': 'everest@moneybloom.in', 'item_name': '456', 'amount': 551.0},
 {'owner': 'blackstone@moneybloom.in',
  'item_name': 'Copper pipe',
  'amount': 600.0},
 {'owner': 'everest@moneybloom.in',
  'item_name': 'Copper pipe',
  'amount': 601.0},
 {'owner': 'shrisai@moneybloom.in', 'item_name': '456', 'amount': 750.0}]
# Filter data for 'shrisai@moneybloom.in'
shrisai_data = [entry for entry in data if entry['owner'] == 'shrisai@moneybloom.in']

# Sort the filtered data by item_name and then by descending amount
sorted_shrisai_data = sorted(shrisai_data, key=lambda x: (x['item_name'], -x['amount']))

# Create a list to store the rank of 'shrisai@moneybloom.in' for each item_name
shrisai_ranks = []

# Iterate through the sorted data and assign ranks
for i, entry in enumerate(sorted_shrisai_data, start=1):
    item_name = entry['item_name']
    amount = entry['amount']
    shrisai_ranks.append({'item_name': item_name, 'rank': i, 'amount': amount})

# Store the result in a variable
result_variable = shrisai_ranks

# Print the result or use the variable as needed
print(result_variable)