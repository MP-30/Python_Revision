# list comprehensio: allow us to create a new list based on existing value of another list

number = [1, -5,0,10,100,67,55,20,34]
new_list = []
for num in number:
    if num % 2 == 0:
        new_list.append(num)
print(new_list)
# or 
new_list1 = [num for num in number if num % 2 ==0]
print("list conprehension--")
print(new_list1)

names = ['Vivek','Aditya', 'Rohit', 'Tommy', 'Aman', 'Mommy', 'Yommi']
new_list2 = [name for name in names if name.startswith('A')]
print(new_list2)

new_list3 = [ name for name in names if len(name) <= 4 ]
print(new_list3)