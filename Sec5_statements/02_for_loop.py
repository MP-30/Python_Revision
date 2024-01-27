my_iterable = [1,2,3]
for item_name in my_iterable:
  print(item_name)
  
my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
  if(num % 2 ==0):
    print(num)
  else:
    print(f'{num}is odd')
    
print("********************")

list_sum = 0
for num in my_list:
  list_sum = list_sum + num
print(f'{num} and sum is {list_sum}')
print("********************")

myString = 'Hello World'
for letter in myString:
  print(letter)
  
print("********************")

tup = (1,2,3)
for item in tup:
  print(item)
  
print("********************")
mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
for item in mylist:
  print(item)
    
  
print("********************")

for (a,b) in mylist:
  print(a)
  print(b)

print("1********************")

mylist = [(1,2,3),(4,5,6),(7,8,9)]
for (a,b,c) in mylist:
  print(a)
  print(b)
  print(c)
  
print("2********************")

d = {'k1': 1, 'k2':2, 'k3': 3}
for item in d.values():
  print(item)