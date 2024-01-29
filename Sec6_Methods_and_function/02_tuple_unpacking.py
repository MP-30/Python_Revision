stock_prices = [('APL',200),('Orange', 500),('Mango',700)]
for item in stock_prices:
  print(item)
  
for ticker, price in stock_prices:
  print(ticker, price + (0.2 * price))
  
work_hours = [('Abby', 100), ('Billy', 4000), ('Casy', 800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    
    for employee, hours in work_hours:
      if hours > current_max:
        current_max = hours
        employee_of_month = employee
    #Return tuple
    return(employee_of_month, current_max)
  
result = employee_check(work_hours)
name , hours = employee_check(work_hours)
print(name)   
print(hours)