x = 10
while x < 5:
  print(x)
  x +=1
else:
  print ("x is not less than 5")
  
print('****************')

x = [1,2,3]
for item in x:
  pass
  print("Passed")
print("Bypassed")
print('****************')
mystring = 'sammy'
for letter in mystring:
  if letter == 'm':
    continue
  print(letter)
  
print('****************')

mystring = 'sammy'
for letter in mystring:
  if letter == 'm':
    break
  print(letter)

print('****************')
x = 0
while x <5:
  if x == 3:
    break
  print(x)
  x +=1