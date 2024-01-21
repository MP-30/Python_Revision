#key value pair
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(my_dict['key1'])
prices_lookup = {'apple': 3.98, 'mangos':50.69, 'banana':85.69}
print(prices_lookup['apple'])
#print(prices_lookup['3.98'])
d = {'k1':132, 'k2':[0,3,2,5,8], 'k3':{'key':589}}
print(d['k2'])
print(d['k3'])
print(d['k3']['key'])
print(d['k2'][2])

d2 = {'key1':['a','b','c']}
mylist =d2['key1'][2]
print(mylist.upper())

d3 = {'k1':100, 'k2':500}
d3['k3'] = 300
d3['k1'] = 'new_value'
print(d3)
print(d3.keys())
print(d3.items())
print(d3.values())