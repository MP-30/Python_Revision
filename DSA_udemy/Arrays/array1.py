my_list = [1,5,10,4, "Aditya",0.5, True]


my_list.append("aditya")
my_list[4] = "Singh"
for a in my_list:
    print(a)

my_list1 = [5,8,6]
my_list.extend(my_list1)
print(my_list)

result = my_list.copy()
result.remove(1)
print(result)

# this is 0(1) because we manipulatae the last item
result = my_list.pop()
print(result)

list_names = ["Bhupi", "aditya", "ayush", "stephen", "ali", "rahul","maria"]
list_names.sort()
print(list_names)
list_int = [45,78,26,98,54,71,26,38,82]
list_int.sort()
print(list_int)