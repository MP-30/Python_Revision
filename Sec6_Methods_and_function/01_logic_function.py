def find_even(a):
  if (a %2 == 0 ):
    return(f'Number {a} is even')
  else:
    return(f'Number {a} is odd')
  
print(find_even(7))

print("********************")
def check_even_list(num_list):
  for number in num_list:
    if number %2 == 0:
      return True
    else:
      pass
  return False
    
print(check_even_list([5,7,5,3,9,12]))
print("********************")
# return all even numbers
def check_even_list1(num_list):
  even_numbers = []
  for number in num_list:
    if number %2 == 0:
      even_numbers.append(number)
    else:
      pass
  return even_numbers
    
print(check_even_list1([5,7,8,3,9,12]))
    