lst = [2, 3, 6, 6, 5]
max_v = 6

new_lst = sorted((lst),reverse=False)
new_index = new_lst.index(max_v) - 1
print(new_lst[new_index])